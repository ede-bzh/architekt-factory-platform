#!/usr/bin/env bash
# Architekt — GitHub project setup (v2 — 7-phase roadmap)
# Crée labels, milestones, issues, et (optionnellement) un Project v2.
#
# Pré-requis :
#   - gh CLI installé et authentifié (gh auth login)
#   - jq, yq installés
#   - Lancé depuis la racine du repo
#
# Usage :
#   bash scripts/github/setup-project.sh                  # tout
#   bash scripts/github/setup-project.sh labels           # uniquement labels
#   bash scripts/github/setup-project.sh milestones       # uniquement milestones
#   bash scripts/github/setup-project.sh issues           # uniquement issues
#   bash scripts/github/setup-project.sh project          # Project v2
#
# Idempotent : skippe ce qui existe déjà.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

REPO_SLUG="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
OWNER="${REPO_SLUG%/*}"

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
# Milestones (7 phases + conditional triggers)
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
  info "Création des milestones Architekt (7-phase roadmap)…"
  local today
  today=$(date -u +%Y-%m-%d)
  iso_plus() { date -u -d "$today +$1 days" +%Y-%m-%dT00:00:00Z 2>/dev/null \
            || date -u -v+"$1"d -j -f "%Y-%m-%d" "$today" +%Y-%m-%dT00:00:00Z; }

  create_milestone "Phase 0 — Foundation & Rebrand"   "Rebrand Architekt + brand system + legal pack + landing placeholder" "$(iso_plus 7)"
  create_milestone "Phase 1 — Offer & Catalog"        "5 offres packagées + catalogue technos tierisé A/B/C + ADR 008-012"   "$(iso_plus 14)"
  create_milestone "Phase 2 — Delivery Doctrine"      "12 skills Architekt + CI verte + SAST/SCA + SBOM + mutation testing" "$(iso_plus 21)"
  create_milestone "Phase 3 — Public Pilot"           "architekt.* live + Lighthouse>=95 + WCAG AA + démo + case study + IMDA application" "$(iso_plus 35)"
  create_milestone "Phase 4 — First Paid Clients"     "3 clients payants signés et livrés, marge mesurée, 2 case studies"    "$(iso_plus 120)"
  create_milestone "Phase 5 — Internal Developer Platform" "Mission/repo/CI/report générés automatiquement en <10 min"      "$(iso_plus 180)"
  create_milestone "Phase 6 — Client Portal"          "Conditionnel — déclencheur 5 clients actifs. Portail read-only."     ""
  create_milestone "Phase 7 — SaaS Option"            "Conditionnel — déclencheur 10+ clients, 3 offres répétables, marge stable" ""
}

# ─────────────────────────────────────────────────────────────────────────────
# Issues
# ─────────────────────────────────────────────────────────────────────────────
issue_exists() {
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
  info "Création des issues Architekt (v2 — 7 phases)…"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 0 — Foundation & Rebrand                                          ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P0] Foundation & Rebrand" \
"Voir docs/architekt/phase-0-rebrand.md.

Sous-tâches :
- [ ] [P0] docs — rebrand README et docs racine
- [ ] [P0] ui — rebrand templates et tokens
- [ ] [P0] config — variables env ARCHITEKT_*
- [ ] [P0] pyproject + CLI alias
- [ ] [P0] brand — palette + typo + voice
- [ ] [P0] legal — NDA + MSA + SOW + DPA templates
- [ ] [P0] landing page placeholder
- [ ] [DECISION] domaine architekt.TBD (issue séparée)
- [ ] [DECISION] couleur de marque (issue séparée)
- [ ] [DECISION] entité légale SG ouverte
- [ ] [ADR-006] licence révisée — propriétaire interne

Gate : marque appliquée partout, anciens noms supprimés visible, licence décidée, templates commerciaux + legal prêts, landing live, CI verte." \
"type:epic,phase:0-foundation,area:rebrand,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] docs — rebrand README et docs racine vers Architekt" \
"README.md (EN) + variantes langues + CODE_OF_CONDUCT + SECURITY + CONTRIBUTING → marque Architekt + positionnement.
Voir docs/architekt/phase-0-rebrand.md (Niveau 1)." \
"type:chore,phase:0-foundation,area:docs,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] ui — rebrand templates et tokens" \
"platform/web/templates/{base,login,onboarding,home}.html → Architekt.
Token CSS --purple → --brand-primary (placeholder valeur identique)." \
"type:chore,phase:0-foundation,area:ui,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] config — variables env ARCHITEKT_*" \
"Introduire ARCHITEKT_API_KEY (alias rétro-compatible MACARON_API_KEY).
Adapter platform/security.py + .env.example + Makefile + scripts.
Documenter dépréciation 6 mois." \
"type:chore,phase:0-foundation,area:platform,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] pyproject + CLI alias architekt" \
"pyproject.toml : name = architekt-factory-platform, entry-point architekt = cli.sf:main.
Garder sf en alias 6 mois." \
"type:chore,phase:0-foundation,area:platform,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] brand — palette + typographies + tone of voice" \
"docs/brand/palette.md (OKLCH 4-6 couleurs)
docs/brand/typography.md (Inter + JetBrains Mono recommandés)
docs/brand/voice.md (pro, technique, pas startup-hype)
Logo placeholder text-based ou Figma simple." \
"type:chore,phase:0-foundation,area:brand,role:designer,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] legal — NDA + MSA + SOW + DPA templates" \
"docs/legal/architekt-nda-template.md (mutual, 1 page)
docs/legal/architekt-msa-template.md (cession IP, clause AI, AUP)
docs/legal/architekt-sow-template.md (par offre)
docs/legal/architekt-dpa-template.md (PDPA SG compliant)
Revue avocat SG dès J5." \
"type:chore,phase:0-foundation,area:legal,role:legal,risk:legal,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[P0] landing page placeholder architekt.TBD" \
"Carrd ou Astro 1-pager, hébergé Cloudflare Pages.
Contenu : Architekt — Coming soon, contact email." \
"type:feature,phase:0-foundation,area:website,priority:should" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[DECISION] Domaine Architekt (architekt.sg / .ai / .io)" \
"Vérifier disponibilité + coût + image marque.
Options : architekt.sg (local SG), architekt.ai (tech), architekt.io (dev), architekt.com (premium).
Deadline : avant Phase 3 (achat domaine pilote)." \
"type:question,status:needs-decision,phase:0-foundation,role:cpo,priority:should" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[DECISION] Couleur de marque Architekt (palette OKLCH)" \
"Définir --brand-primary et --brand-secondary.
Pistes : conserver purple, ou changer (bleu deep, vert sage, ardoise, rouge brique).
Livrable : docs/brand/palette.md + tokens shadcn." \
"type:question,status:needs-decision,phase:0-foundation,role:designer,priority:should" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[DECISION] Entité légale Architekt Pte. Ltd. (Singapour)" \
"Ouvrir entité ACRA (~2 semaines).
Compte bancaire SG.
GST si revenue > 1M SGD/an (sinon optionnel).
Décider si nominee director nécessaire (résidence SG)." \
"type:question,status:needs-decision,phase:0-foundation,role:cpo,risk:legal,priority:must" \
"Phase 0 — Foundation & Rebrand"

  create_issue "[ADR-006] Licence — propriétaire interne (révisé)" \
"Voir docs/adr/006-license.md (révisé).
Recommandation : propriétaire interne par défaut + composants publiables MIT/Apache à la pièce.
Action : valider avec avocat SG avant 1er contrat client." \
"type:adr,phase:0-foundation,risk:legal,role:cto,priority:must,status:needs-decision" \
"Phase 0 — Foundation & Rebrand"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 1 — Offer & Stack Catalogue                                       ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P1] Offer & Stack Catalogue" \
"Voir docs/architekt/phase-1-offer-catalog.md, docs/OFFERS.md, docs/CATALOG.md.

Sous-tâches :
- [ ] [P1] 5 offres one-pagers (Launch, MVP, Internal Tool, AI Workflow, Audit)
- [ ] [P1] 5 SOW templates par offre
- [ ] [P1] FinOps par offre (budget LLM + heures + marge)
- [ ] [P1] intake checklist accept/refuse
- [ ] [P1] catalogue tierisé revue
- [ ] [P1] 17 squelettes docs/catalog/*.md
- [ ] [ADR-008] Offers before stacks
- [ ] [ADR-009] Internal platform before SaaS
- [ ] [ADR-010] Human approval policy for agents
- [ ] [ADR-011] LLM cost governance
- [ ] [ADR-012] SBOM and supply-chain baseline" \
"type:epic,phase:1-offers,area:offers,area:catalog,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[P1] 5 one-pagers offres (Launch / MVP / Internal Tool / AI Workflow / Audit)" \
"Pour chaque offre dans docs/OFFERS.md :
- 1 page Markdown
- Export PDF
- À envoyer aux prospects" \
"type:chore,phase:1-offers,area:offers,role:pmm,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[P1] 5 SOW templates (un par offre)" \
"docs/legal/sow-{launch,mvp,internal-tool,ai-workflow,audit}-template.md.
Structure standard (Contexte, Périmètre, Livrables, Stack, Planning, Équipe, Prix, IP/AI, Garanties)." \
"type:chore,phase:1-offers,area:legal,area:offers,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[P1] FinOps par offre (budget LLM + heures + marge cible)" \
"Documenter dans docs/OFFERS.md tableau FinOps :
| Offre | Budget LLM | Heures max | Infra | Marge cible |
Cohérent avec ADR-011 et ADR-016." \
"type:chore,phase:1-offers,area:finops,role:cfo,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[P1] intake checklist accept/refuse projet" \
"docs/intake-checklist.md.
Critères BANT + Architekt-specific (Tier stack, IP/AI compatible, secteur).
Cf. skill architekt-commercial.spec.md." \
"type:chore,phase:1-offers,area:offers,role:cpo,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[P1] catalog — 17 squelettes docs/catalog/*.md" \
"Pour chaque stack Tier A/B/C, créer docs/catalog/<stack>.md vide (rempli quand activé).
Stacks Tier A (7) + Tier B (7) + Tier C (3) = 17." \
"type:chore,phase:1-offers,area:catalog,area:docs,priority:should" \
"Phase 1 — Offer & Catalog"

  create_issue "[ADR-008] Offers before stacks" \
"Voir docs/adr/008-offers-before-stacks.md.
Vendre par outcome (5 offres), pas par stack." \
"type:adr,phase:1-offers,role:cpo,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[ADR-009] Internal platform before SaaS" \
"Voir docs/adr/009-internal-platform-before-saas.md.
Studio d'abord (3 clients), IDP (5), SaaS éventuellement (10+)." \
"type:adr,phase:1-offers,role:cpo,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[ADR-010] Human approval policy for agents" \
"Voir docs/adr/010-human-approval-policy.md.
L0-L4 classification, HITL obligatoire L3+." \
"type:adr,phase:1-offers,role:cto,role:caio,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[ADR-011] LLM cost governance (FinOps)" \
"Voir docs/adr/011-llm-cost-governance.md.
Budget par mission, alertes 70/90/100%, auto-pause." \
"type:adr,phase:1-offers,area:finops,role:cto,role:cfo,priority:must" \
"Phase 1 — Offer & Catalog"

  create_issue "[ADR-012] SBOM and supply-chain baseline" \
"Voir docs/adr/012-sbom-supply-chain-baseline.md.
CycloneDX/SPDX, NIST SSDF PS.3.2 obligatoire." \
"type:adr,phase:1-offers,area:security,role:ciso,priority:must" \
"Phase 1 — Offer & Catalog"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 2 — Delivery Doctrine                                             ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P2] Delivery Doctrine + CI sécurité" \
"Voir docs/architekt/phase-2-practices.md.

Sous-tâches :
- [ ] [P2] 6 skills enrichis (archi, tech, ux, data, security, sre)
- [ ] [P2] 6 skills nouveaux (delivery, product, finops, ai-governance, commercial, qa)
- [ ] [P2] CI baseline (.github/workflows/ci.yml)
- [ ] [P2] SAST (bandit) + SCA (safety) + secret scan (trufflehog)
- [ ] [P2] SBOM CycloneDX au build
- [ ] [P2] Mutation testing modules critiques (seuil 50%)
- [ ] [P2] Badge CI README
- [ ] [P2] Baseline qualité docs/quality-baseline.md
- [ ] [ADR-013] Client IP / AI-generated code policy
- [ ] [ADR-014] WCAG 2.2 AA baseline
- [ ] [ADR-015] Quality Report as commercial artifact" \
"type:epic,phase:2-doctrine,area:agents,area:ci,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] CI baseline (pytest + ruff + bandit + safety + trufflehog)" \
"Voir docs/architekt/phase-2-practices.md squelette workflow.
- [ ] CI verte sur PR de cette issue
- [ ] Badge README
- [ ] Run < 5 min" \
"type:chore,phase:2-doctrine,area:ci,role:cto,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-delivery — implementation" \
"À partir de docs/skills-spec/architekt-delivery.spec.md, créer skills/architekt-delivery.md.
Phases discovery/build/hardening/handover, DoD, scope rules, kill criteria." \
"type:skill,phase:2-doctrine,area:agents,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-finops — implementation" \
"À partir de docs/skills-spec/architekt-finops.spec.md, créer skills/architekt-finops.md.
Budget LLM/mission, alertes, marges cibles par offre." \
"type:skill,phase:2-doctrine,area:agents,area:finops,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-ai-governance — implementation" \
"À partir de docs/skills-spec/architekt-ai-governance.spec.md, créer skills/architekt-ai-governance.md.
HITL workflow, audit log policy, client data residency, transparence." \
"type:skill,phase:2-doctrine,area:agents,area:security,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-commercial — implementation" \
"À partir de docs/skills-spec/architekt-commercial.spec.md, créer skills/architekt-commercial.md.
BANT qualification, devis <48h, négociation, pipeline." \
"type:skill,phase:2-doctrine,area:agents,area:gtm,priority:should" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-product — implementation" \
"À partir de docs/skills-spec/architekt-product.spec.md, créer skills/architekt-product.md.
Discovery, JTBD, hypothèses, personas, métriques." \
"type:skill,phase:2-doctrine,area:agents,role:cpo,priority:should" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] skill architekt-qa — implementation" \
"À partir de docs/skills-spec/architekt-qa.spec.md, créer skills/architekt-qa.md.
Mutation testing ciblé, a11y audit, perf, security scan, Quality Report gates." \
"type:skill,phase:2-doctrine,area:agents,area:ci,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[P2] 6 skills techniques enrichis (archi, tech, ux, data, security, sre)" \
"Mettre à jour les 6 skills techniques existants selon docs/skills-spec/.
Référencer les ADR pertinents." \
"type:skill,phase:2-doctrine,area:agents,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[ADR-013] Client IP and AI-generated code policy" \
"Voir docs/adr/013-client-ip-ai-code-policy.md.
Cession totale code client, transparence IA, data residency." \
"type:adr,phase:2-doctrine,role:cpo,role:legal,risk:legal,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[ADR-014] Accessibility WCAG 2.2 AA baseline" \
"Voir docs/adr/014-a11y-wcag-baseline.md.
axe-core CI obligatoire, audit composants shadcn (corrections nécessaires)." \
"type:adr,phase:2-doctrine,role:designer,priority:must" \
"Phase 2 — Delivery Doctrine"

  create_issue "[ADR-015] Quality Report as commercial artifact" \
"Voir docs/adr/015-quality-report-commercial-artifact.md.
10 dimensions + DORA + SBOM, livré à chaque mission." \
"type:adr,phase:2-doctrine,role:cpo,role:pmm,priority:must" \
"Phase 2 — Delivery Doctrine"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 3 — Public Pilot                                                  ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P3] Public Pilot — site Architekt live + actif commercial" \
"Voir docs/architekt/phase-3-pilot.md.
Site Astro + pages Method/Platform/Proof + démo vidéo + case study + Quality Report public.

Sous-tâches :
- [ ] [P3] VM Hetzner CAX11 + déploiement plateforme
- [ ] [P3] HTTPS + auth fail-closed
- [ ] [P3] Domaine architekt.TBD + DNS
- [ ] [P3] Mission idéation site Architekt
- [ ] [P3] Site Astro + Tailwind + shadcn (auto-généré par plateforme)
- [ ] [P3] Audit a11y manuel (axe + screen reader)
- [ ] [P3] Lighthouse >= 95
- [ ] [P3] Plausible analytics
- [ ] [P3] Démo vidéo 2 min
- [ ] [P3] Case study fictif réaliste
- [ ] [P3] Quality Report public sur /proof
- [ ] [P3] Candidature IMDA SME Digital Solutions
- [ ] [ADR-016] Pricing model and margin targets
- [ ] [ADR-017] Cloud deployment decision matrix" \
"type:epic,phase:3-pilot,area:website,area:deploy,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[P3] VM Hetzner CAX11 + déploiement plateforme Architekt" \
"Cf. ADR-005 et ADR-017.
- [ ] Compte Hetzner créé
- [ ] CAX11 provisionné (Helsinki ou Hillsboro)
- [ ] Docker installé, clone repo
- [ ] platform up via docker compose
- [ ] ARCHITEKT_API_KEY générée et stockée
- [ ] Backups snapshots quotidiens activés" \
"type:chore,phase:3-pilot,area:deploy,role:sre,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Achat domaine architekt.TBD + DNS Cloudflare + HTTPS" \
"Une fois décision domaine tranchée :
- [ ] Achat (Namecheap, OVH ou Cloudflare Registrar)
- [ ] DNS Cloudflare
- [ ] CNAME platform.architekt.TBD → VM Hetzner
- [ ] CNAME architekt.TBD → Cloudflare Pages
- [ ] HTTPS Caddy ou Traefik sur platform.*" \
"type:chore,phase:3-pilot,area:deploy,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Mission plateforme : site Architekt (Astro 5)" \
"Lancer mission idéation avec brief de docs/architekt/phase-3-pilot.md.
Stack : Astro 5 + Tailwind v4 + shadcn/ui.
Pages : Home, Offres, Method, Platform, Proof, Team, Contact, Blog.
Langues : EN + FR + ZH." \
"type:feature,phase:3-pilot,area:website,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Audit a11y WCAG 2.2 AA (axe-core + manuel)" \
"axe-core en CI Playwright, Pa11y CLI, audit manuel composants shadcn.
Gate : aucun fail critique/serious." \
"type:chore,phase:3-pilot,area:website,role:designer,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Démo vidéo 2 minutes + post LinkedIn" \
"Mission agentique → livrable (Loom ou OBS).
Publier sur LinkedIn + YouTube unlisted + embed sur /proof." \
"type:chore,phase:3-pilot,area:gtm,role:pmm,priority:should" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Case study fictif réaliste pour /proof" \
"Sujet : How Architekt would deliver a SaaS MVP for ACME (B2B SG).
Contenu : brief, équipe, timeline, livrables, métriques, Quality Report.
Format : page web + PDF exportable." \
"type:chore,phase:3-pilot,area:website,role:pmm,priority:should" \
"Phase 3 — Public Pilot"

  create_issue "[P3] Candidature IMDA SME Digital Solutions vendor list" \
"Cf. docs/GTM.md canal 1.
Préparer dossier : entité SG, case study, conformité, pricing.
Soumettre à IMDA — process 1-2 mois." \
"type:chore,phase:3-pilot,area:gtm,role:cpo,priority:should" \
"Phase 3 — Public Pilot"

  create_issue "[ADR-016] Pricing model and margin targets" \
"Voir docs/adr/016-pricing-and-margins.md.
Forfait par offre, marge brute >50%, modalités 30/40/30, currency SGD." \
"type:adr,phase:3-pilot,area:offers,area:finops,role:cpo,role:cfo,priority:must" \
"Phase 3 — Public Pilot"

  create_issue "[ADR-017] Cloud deployment decision matrix" \
"Voir docs/adr/017-cloud-decision-matrix.md.
Cloudflare/Hetzner/Fly par défaut, AWS/Azure/GCP si client impose." \
"type:adr,phase:3-pilot,area:deploy,role:cto,role:sre,priority:must" \
"Phase 3 — Public Pilot"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 4 — First Paid Clients                                            ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P4] First Paid Clients — 3 clients, marge mesurée, répétabilité" \
"Voir docs/architekt/phase-4-first-clients.md.

Métriques : marge >50%, NPS >8, rework <15%, 0 P1/P2 bugs.

Sous-tâches :
- [ ] [P4] 3 canaux acquisition actifs en parallèle
- [ ] [P4] CRM configuré (Notion / Airtable / Pipedrive)
- [ ] [P4] facturation (Stripe / Xero / accounting SG)
- [ ] [P4] 3 clients payants signés et livrés
- [ ] [P4] 2 case studies réels publiés
- [ ] [P4] marge brute mesurée et communicable
- [ ] [P4] 1 client récurrent (TMA/Run)
- [ ] [P4] spec phase-6-client-portal détaillée
- [ ] [P4] retros post-mission complètes
- [ ] [ADR-018] Data retention and client isolation
- [ ] [ADR-019] Agent audit logs and reproducibility
- [ ] [ADR-020] When to introduce multi-tenancy" \
"type:epic,phase:4-clients,area:gtm,priority:must" \
"Phase 4 — First Paid Clients"

  create_issue "[P4] 3 canaux acquisition actifs (IMDA + LinkedIn + Content)" \
"Démarrer en parallèle :
- IMDA pre-approved vendor (candidature déposée Phase 3)
- LinkedIn outbound 50 messages/sem
- Content : 1 post/sem blog Architekt + LinkedIn newsletter
Mesurer ROI à 3 mois." \
"type:feature,phase:4-clients,area:gtm,role:gtm,role:cpo,priority:must" \
"Phase 4 — First Paid Clients"

  create_issue "[P4] CRM + facturation opérationnels" \
"CRM : Notion / Airtable / Pipedrive (choisir).
Facturation : Stripe (SaaS-friendly) ou Xero (accounting SG).
Compte bancaire SG opérationnel.
GST si applicable." \
"type:chore,phase:4-clients,area:gtm,role:cfo,priority:must" \
"Phase 4 — First Paid Clients"

  create_issue "[ADR-018] Data retention and client isolation" \
"Voir docs/adr/018-data-retention-isolation.md.
Isolation par client (repo, vault, DB), rétention par type, anonymisation, PDPA/RGPD." \
"type:adr,phase:4-clients,area:security,role:ciso,role:legal,priority:must" \
"Phase 4 — First Paid Clients"

  create_issue "[ADR-019] Agent audit logs and reproducibility" \
"Voir docs/adr/019-agent-audit-reproducibility.md.
Append-only hash chain, 90j actif + 1an archive, exportable client." \
"type:adr,phase:4-clients,area:security,role:cto,role:caio,priority:must" \
"Phase 4 — First Paid Clients"

  create_issue "[ADR-020] When to introduce multi-tenancy" \
"Voir docs/adr/020-when-multi-tenancy.md.
Triggers stricts (5 clients pour Phase 6, 10+ pour Phase 7)." \
"type:adr,phase:4-clients,role:cto,role:cpo,priority:should" \
"Phase 4 — First Paid Clients"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 5 — IDP                                                            ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P5] Internal Developer Platform (mission → deploy en <10 min)" \
"Voir docs/architekt/phase-5-idp.md.

10 capacités à construire (mission manifest, agent registry, template registry,
environment provisioning Terraform, secrets management, CI templates, quality
scanner API, cost tracker, audit trail, client report generator).

Démarre après 3 clients livrés (Phase 4)." \
"type:epic,phase:5-idp,area:idp,area:platform,role:cto,priority:should" \
"Phase 5 — Internal Developer Platform"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Phase 6 & 7 — Conditional                                                ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[EPIC][P6] Client Portal (déclencheur 5 clients actifs)" \
"Voir docs/architekt/phase-6-client-portal.md.

Conditionnel — démarrer SEULEMENT après trigger.
Portail read-only : statut, livrables, rapports, ADR, factures, feedback, roadmap." \
"type:epic,phase:6-portal,area:portal,status:trigger-pending,priority:could" \
"Phase 6 — Client Portal"

  create_issue "[EPIC][P7] SaaS Option (déclencheur 10+ clients + marge stable)" \
"Voir docs/architekt/phase-7-saas.md.

Conditionnel STRICT — démarrer SEULEMENT après tous triggers.
Multi-tenant + billing + SSO + marketplace.

Décision formelle requise : docs/decisions/saas-go-no-go.md" \
"type:epic,phase:7-saas,area:saas,status:trigger-pending,priority:could" \
"Phase 7 — SaaS Option"

  # ╔══════════════════════════════════════════════════════════════════════════╗
  # ║  Risk tracking (P1 risks permanently open)                                ║
  # ╚══════════════════════════════════════════════════════════════════════════╝

  create_issue "[RISK-P1] R1 Pas de pipeline commercial (CRITIQUE)" \
"Cf. docs/RISKS.md R1.
Indicateur : leads qualifiés / mois.
Trigger escalade : 0 lead 4 semaines consécutives." \
"type:question,risk:pipeline,role:cpo,priority:must,status:trigger-pending" \
""

  create_issue "[RISK-P1] R2 Delivery non rentable / marge < 50% (CRITIQUE)" \
"Cf. docs/RISKS.md R2.
Indicateur : marge brute par projet.
Trigger : marge < 40% sur 1 projet → revue ; sur 2 → freeze nouveaux contrats." \
"type:question,risk:margin,role:cpo,role:cto,priority:must,status:trigger-pending" \
""

  create_issue "[RISK-P1] R3 Coût LLM invisible / dérive" \
"Cf. docs/RISKS.md R3.
Indicateur : ratio coût LLM réel/budget par mission.
Trigger : dépassement >20% sur 1 mission → audit ; sur 3 → cut-off durci." \
"type:question,risk:llm-cost,role:cto,priority:must,status:trigger-pending" \
""

  ok "Issues Architekt créées (v2)."
}

# ─────────────────────────────────────────────────────────────────────────────
# Project v2 (optionnel)
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
