#!/usr/bin/env bash
# Architekt — GitHub project setup
# Crée labels, milestones, issues, et (optionnellement) un Project v2.
#
# Pré-requis :
#   - gh CLI installé et authentifié (gh auth login)
#   - jq, yq installés
#   - Lancé depuis la racine du repo (le script auto-détecte)
#
# Usage :
#   bash scripts/github/setup-project.sh                  # tout (labels + milestones + issues)
#   bash scripts/github/setup-project.sh labels           # uniquement labels
#   bash scripts/github/setup-project.sh milestones       # uniquement milestones
#   bash scripts/github/setup-project.sh issues           # uniquement issues
#   bash scripts/github/setup-project.sh project          # crée le Project v2 (org/user)
#
# Idempotent : skippe ce qui existe déjà.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

REPO_SLUG="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
OWNER="${REPO_SLUG%/*}"

# Couleurs terminal
RED=$'\033[31m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; BLUE=$'\033[34m'; NC=$'\033[0m'
info() { echo "${BLUE}[info]${NC} $*"; }
ok()   { echo "${GREEN}[ok]${NC}   $*"; }
warn() { echo "${YELLOW}[warn]${NC} $*"; }
die()  { echo "${RED}[err]${NC}  $*" >&2; exit 1; }

command -v gh >/dev/null  || die "gh CLI manquant — https://cli.github.com"
command -v jq >/dev/null  || die "jq manquant"
command -v yq >/dev/null  || die "yq manquant (mikefarah/yq)"

# ─────────────────────────────────────────────────────────────────────────────
# Labels
# ─────────────────────────────────────────────────────────────────────────────
setup_labels() {
  info "Création des labels depuis .github/labels.yml…"
  local count=0
  while IFS= read -r entry; do
    local name color desc
    name=$(echo "$entry" | yq '.name' -)
    color=$(echo "$entry" | yq '.color' -)
    desc=$(echo "$entry" | yq '.description' -)
    if gh label list --limit 200 --json name -q '.[].name' | grep -Fxq "$name"; then
      gh label edit "$name" --color "$color" --description "$desc" >/dev/null
      ok "label mis à jour : $name"
    else
      gh label create "$name" --color "$color" --description "$desc" >/dev/null
      ok "label créé      : $name"
    fi
    count=$((count + 1))
  done < <(yq -o=json '.[]' .github/labels.yml | jq -c '.')
  info "Labels traités : $count"
}

# ─────────────────────────────────────────────────────────────────────────────
# Milestones
# ─────────────────────────────────────────────────────────────────────────────
milestone_exists() {
  gh api "repos/$REPO_SLUG/milestones?state=all" -q ".[] | select(.title == \"$1\") | .number" 2>/dev/null
}

create_milestone() {
  local title="$1" desc="$2" due="$3"
  if [ -n "$(milestone_exists "$title")" ]; then
    ok "milestone existe : $title"
    return
  fi
  if [ -n "$due" ]; then
    gh api "repos/$REPO_SLUG/milestones" -f title="$title" -f description="$desc" -f due_on="$due" -X POST >/dev/null
  else
    gh api "repos/$REPO_SLUG/milestones" -f title="$title" -f description="$desc" -X POST >/dev/null
  fi
  ok "milestone créé  : $title"
}

setup_milestones() {
  info "Création des milestones Architekt…"
  # Date due : par défaut +N jours à partir d'aujourd'hui
  local today
  today=$(date -u +%Y-%m-%d)
  iso_plus() { date -u -d "$today +$1 days" +%Y-%m-%dT00:00:00Z 2>/dev/null \
            || date -u -v+"$1"d -j -f "%Y-%m-%d" "$today" +%Y-%m-%dT00:00:00Z; }

  create_milestone "Phase 0 — Rebrand"        "Tout le repo + UI portent la marque Architekt." "$(iso_plus 7)"
  create_milestone "Phase 1 — Catalog & ADR"  "Catalogue technos + 6 ADR mergés."               "$(iso_plus 14)"
  create_milestone "Phase 2 — Doctrine & CI"  "6 skills doctrine + CI verte."                   "$(iso_plus 21)"
  create_milestone "Phase 3 — Pilot website"  "Site Architekt en ligne."                        "$(iso_plus 35)"
  create_milestone "Phase 4 — On-demand"      "Activation kits à la demande (continu)."         ""
}

# ─────────────────────────────────────────────────────────────────────────────
# Issues
# ─────────────────────────────────────────────────────────────────────────────
issue_exists() {
  # Match exact sur le titre (open + closed)
  gh issue list --state all --search "in:title \"$1\"" --json title -q '.[].title' \
    | grep -Fxq "$1"
}

create_issue() {
  local title="$1" body="$2" labels="$3" milestone="$4"
  if issue_exists "$title"; then
    ok "issue existe   : $title"
    return
  fi
  local args=(--title "$title" --body "$body")
  [ -n "$labels" ]    && args+=(--label "$labels")
  [ -n "$milestone" ] && args+=(--milestone "$milestone")
  gh issue create "${args[@]}" >/dev/null
  ok "issue créée    : $title"
}

setup_issues() {
  info "Création des issues Architekt…"

  # ── Phase 0 ──
  create_issue "[EPIC][P0] Rebrand Architekt" \
"Voir docs/architekt/phase-0-rebrand.md et docs/adr/001-rebrand-architekt.md.

Sous-tâches :
- [ ] [P0] docs — rebrand README et docs racine
- [ ] [P0] ui — rebrand templates et tokens
- [ ] [P0] config — variables env ARCHITEKT_*
- [ ] [P0] pyproject + CLI alias
- [ ] [DECISION] domaine architekt.TBD
- [ ] [DECISION] couleur de marque
- [ ] [DECISION] licence (ADR-006)

Gate : CI verte + PR mergée + UI cohérente Architekt." \
"type:epic,phase:0-rebrand,area:rebrand,priority:must" \
"Phase 0 — Rebrand"

  create_issue "[P0] docs — rebrand README et docs racine" \
"README.md (EN) + variantes langues + CODE_OF_CONDUCT + SECURITY + CONTRIBUTING → marque Architekt.

Voir docs/architekt/phase-0-rebrand.md (Niveau 1).
Ne pas toucher README.laposte.md (sync interne)." \
"type:chore,phase:0-rebrand,area:docs,priority:must" \
"Phase 0 — Rebrand"

  create_issue "[P0] ui — rebrand templates et tokens" \
"platform/web/templates/{base,login,onboarding,home}.html → Architekt.
Token CSS --purple → --brand-primary (valeur inchangée tant que couleur non tranchée)." \
"type:chore,phase:0-rebrand,area:ui,priority:must" \
"Phase 0 — Rebrand"

  create_issue "[P0] config — variables env ARCHITEKT_*" \
"Introduire ARCHITEKT_API_KEY (alias rétro-compatible MACARON_API_KEY).
Adapter platform/security.py + .env.example + Makefile + scripts.
Documenter dépréciation soft sur 6 mois." \
"type:chore,phase:0-rebrand,area:platform,priority:must" \
"Phase 0 — Rebrand"

  create_issue "[P0] pyproject + CLI alias architekt" \
"pyproject.toml : name = architekt-factory-platform, entry-point architekt = cli.sf:main.
Garder sf en alias 6 mois.
Mettre à jour doc CLI." \
"type:chore,phase:0-rebrand,area:platform,priority:must" \
"Phase 0 — Rebrand"

  create_issue "[DECISION] Domaine Architekt (architekt.sg / .ai / .io)" \
"Vérifier disponibilité + coût + image marque.
Options : architekt.sg (local SG), architekt.ai (tech), architekt.io (dev), architekt.com (premium).
Deadline souhaitée : avant Phase 3 (achat domaine pilote)." \
"type:question,status:needs-decision,phase:0-rebrand,role:cpo,priority:should" \
"Phase 0 — Rebrand"

  create_issue "[DECISION] Couleur de marque Architekt (palette)" \
"Définir --brand-primary, --brand-secondary en OKLCH.
Pistes : conserver purple, ou changer (bleu deep, vert sage, ardoise, rouge brique).
Livrable : palette dans docs/adr/00X-brand-color.md + tokens shadcn." \
"type:question,status:needs-decision,phase:0-rebrand,role:designer,priority:should" \
"Phase 0 — Rebrand"

  create_issue "[ADR-006] Choix de licence (open-core ?)" \
"Voir docs/adr/006-license.md. Recommandation : AGPL-3.0 noyau + MIT skills.
Action : valider avec avocat SG avant 1er contrat client." \
"type:adr,phase:0-rebrand,risk:legal,role:cto,priority:must,status:needs-decision" \
"Phase 0 — Rebrand"

  # ── Phase 1 ──
  create_issue "[EPIC][P1] Catalogue technos & ADR" \
"Voir docs/CATALOG.md et docs/adr/.

Sous-tâches :
- [ ] [ADR-001] Rebrand (déjà écrit, à merger)
- [ ] [ADR-002] Modular Monolith par défaut
- [ ] [ADR-003] Mutation testing (Stryker/mutmut/PIT)
- [ ] [ADR-004] Design system (shadcn+Radix+Tailwind v4)
- [ ] [ADR-005] Hébergement pilote
- [ ] Squelettes docs/catalog/*.md (8 stacks ⚠️)" \
"type:epic,phase:1-catalog,area:catalog,priority:must" \
"Phase 1 — Catalog & ADR"

  create_issue "[P1] catalog — 8 squelettes docs/catalog/*.md" \
"Pour chaque stack ⚠️ du catalogue, créer un docs/catalog/<stack>.md vide.
Stacks : astro, nextjs, nuxt, wordpress, shopify, nestjs, spring-modulith, payload." \
"type:chore,phase:1-catalog,area:catalog,area:docs,priority:should" \
"Phase 1 — Catalog & ADR"

  # ── Phase 2 ──
  create_issue "[EPIC][P2] Doctrine bonnes pratiques + CI" \
"Voir docs/architekt/phase-2-practices.md.

Sous-tâches :
- [ ] [P2] skill architekt-archi.md (modular monolith)
- [ ] [P2] skill architekt-tech.md (TDD + mutation testing + 12-Factor)
- [ ] [P2] skill architekt-ux.md (shadcn + Radix + Tailwind v4)
- [ ] [P2] skill architekt-data.md (PostgreSQL, migrations)
- [ ] [P2] skill architekt-security.md (SAST, OWASP, secrets)
- [ ] [P2] skill architekt-sre.md (SLO, error budget)
- [ ] [P2] CI GitHub Actions pytest + ruff + bandit
- [ ] [P2] Makefile test corrigé
- [ ] [P2] Badge CI README" \
"type:epic,phase:2-practices,area:agents,area:ci,priority:must" \
"Phase 2 — Doctrine & CI"

  create_issue "[P2] CI GitHub Actions pytest + ruff + bandit" \
"Voir docs/architekt/phase-2-practices.md (squelette workflow).
Critères :
- [ ] CI verte sur cette PR
- [ ] Badge ajouté README
- [ ] Run < 5 min" \
"type:chore,phase:2-practices,area:ci,priority:must" \
"Phase 2 — Doctrine & CI"

  create_issue "[P2] skills doctrine Architekt (6 fichiers)" \
"Créer skills/architekt-{archi,tech,ux,data,security,sre}.md selon le format de skills/tdd.md.
Charger les ADR pertinents en référence." \
"type:feature,phase:2-practices,area:agents,priority:must" \
"Phase 2 — Doctrine & CI"

  create_issue "[P2] Makefile test corrigé + dépendances pytest" \
"Le make test actuel pointe sur des fichiers inexistants (test_cache.py, etc.).
Action : remplacer par 'pytest tests/ -q' et lister deps dans pyproject extras dev." \
"type:chore,phase:2-practices,area:ci,priority:must" \
"Phase 2 — Doctrine & CI"

  # ── Phase 3 ──
  create_issue "[EPIC][P3] Pilote site Architekt en ligne" \
"Voir docs/architekt/phase-3-pilot.md.
Stack : Astro 5 + Tailwind v4 + shadcn/ui, hébergement Cloudflare Pages.

Sous-tâches :
- [ ] [P3] VM Hetzner CAX11 + déploiement plateforme
- [ ] [P3] domaine architekt.TBD acheté + DNS
- [ ] [P3] HTTPS via Caddy ou Traefik
- [ ] [P3] mission idéation site Architekt
- [ ] [P3] code généré + push GitHub architekt-website
- [ ] [P3] Cloudflare Pages branchée + deploy
- [ ] [P3] Plausible analytics
- [ ] [P3] case study interne écrit
- [ ] [P3] Lighthouse >= 95 + a11y AA + Stryker >= 60%" \
"type:epic,phase:3-pilot,area:website,area:deploy,priority:must" \
"Phase 3 — Pilot website"

  create_issue "[P3] VM Hetzner CAX11 + déploiement plateforme" \
"Voir ADR-005.
- [ ] Compte Hetzner créé + carte CB
- [ ] CAX11 provisionné (Helsinki ou Hillsboro)
- [ ] Docker installé, clone repo
- [ ] platform up via docker compose
- [ ] ARCHITEKT_API_KEY générée et stockée" \
"type:chore,phase:3-pilot,area:deploy,priority:must" \
"Phase 3 — Pilot website"

  create_issue "[P3] Achat domaine architekt.TBD + DNS Cloudflare" \
"Cf. décision domaine. Une fois tranchée :
- [ ] Achat (Namecheap, OVH ou Cloudflare Registrar)
- [ ] DNS sur Cloudflare
- [ ] CNAME platform.architekt.TBD → VM Hetzner
- [ ] CNAME architekt.TBD → Cloudflare Pages" \
"type:chore,phase:3-pilot,area:deploy,priority:must" \
"Phase 3 — Pilot website"

  create_issue "[P3] Mission plateforme : site Architekt (Astro)" \
"Lancer une mission idéation avec le brief de docs/architekt/phase-3-pilot.md.
Suivre /live, ajuster prompts si dérive." \
"type:feature,phase:3-pilot,area:website,priority:must" \
"Phase 3 — Pilot website"

  create_issue "[P3] Case study site Architekt" \
"Écrire docs/case-studies/architekt-website.md :
- temps total, coût LLM, nombre missions, % rejet
- captures écran avant/après
- ce qui a marché / pas marché
Sert au blog + GTM." \
"type:chore,phase:3-pilot,area:docs,priority:should" \
"Phase 3 — Pilot website"

  # ── Phase 4 (placeholders triggers) ──
  create_issue "[EPIC][P4] Équipement à la demande (continu)" \
"Voir docs/architekt/phase-4-on-demand.md.

Toujours ouvert. Sous-issues créées au fur et à mesure (label kit:<stack>)." \
"type:epic,phase:4-on-demand,priority:could" \
"Phase 4 — On-demand"

  ok "Issues Architekt créées."
}

# ─────────────────────────────────────────────────────────────────────────────
# Project v2 (optionnel — peut nécessiter scope gh project)
# ─────────────────────────────────────────────────────────────────────────────
setup_project() {
  info "Tentative de création d'un Project v2 'Architekt Roadmap'…"
  if ! gh project list --owner "$OWNER" >/dev/null 2>&1; then
    warn "gh project non accessible (scope manquant ?). Re-login : gh auth refresh -s project,read:project"
    warn "Sinon créez le Project manuellement (voir .github/PROJECT.md)."
    return
  fi

  local existing
  existing=$(gh project list --owner "$OWNER" --format json -q '.projects[] | select(.title == "Architekt Roadmap") | .number' || echo "")
  if [ -n "$existing" ]; then
    ok "Project existe (numéro $existing) — Architekt Roadmap"
  else
    gh project create --owner "$OWNER" --title "Architekt Roadmap" >/dev/null
    ok "Project créé — Architekt Roadmap"
  fi

  info "(Configuration des vues/fields à faire dans l'UI — voir .github/PROJECT.md)"
}

# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────
TARGET="${1:-all}"
case "$TARGET" in
  labels)     setup_labels ;;
  milestones) setup_milestones ;;
  issues)     setup_issues ;;
  project)    setup_project ;;
  all)        setup_labels; setup_milestones; setup_issues
              info "Pour créer aussi le Project v2 : bash $0 project" ;;
  *)          die "usage : $0 [labels|milestones|issues|project|all]" ;;
esac

ok "Terminé."
