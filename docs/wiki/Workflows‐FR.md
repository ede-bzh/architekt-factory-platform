# Workflows (41 intégrés)

Chaque workflow définit une séquence de phases exécutées par des agents spécialisés. Les modèles intégrés sont chargés depuis `platform/workflows/builtins.py` et les YAML sous `platform/workflows/templates/`.

## Cycle de vie
| Workflow | Phases | Description |
|----------|--------|-------------|
| `product-lifecycle` | 11 | Livraison produit complète (idéation → déploiement → TMA) |
| `feature-sprint` | 5 | Implémentation de fonctionnalité sur un sprint |
| `feature-request` | 6 | Traitement des demandes de fonctionnalité |

## DSI
| Workflow | Phases | Description |
|----------|--------|-------------|
| `dsi-platform-features` | 9 | Développement de fonctionnalités plateforme |
| `dsi-platform-tma` | 6 | Maintenance plateforme |

## Sécurité
| Workflow | Phases | Description |
|----------|--------|-------------|
| `security-hacking` | 8 | Audit sécurité complet (recon → exploit → rapport) |
| `sast-continuous` | 4 | Analyse statique continue |

## TMA (maintenance)
| Workflow | Phases | Description |
|----------|--------|-------------|
| `tma-maintenance` | 4 | Cycle de maintenance standard |
| `tma-autoheal` | 4 | Opérations d'auto-guérison |

## SAFe
| Workflow | Phases | Description |
|----------|--------|-------------|
| `pi-planning` | 5 | Planification Program Increment |
| `epic-decompose` | 5 | Décomposition Epic → Feature → Story |

## Mobile
| Workflow | Phases | Description |
|----------|--------|-------------|
| `mobile-ios-epic` | 5 | Livraison epic iOS |
| `mobile-android-epic` | 5 | Livraison epic Android |

## Qualité
| Workflow | Phases | Description |
|----------|--------|-------------|
| `documentation-pipeline` | 6 | Docs API → ADR → changelog → docs utilisateur |
| `performance-testing` | 5 | Charge k6 → analyse → boucle correctifs → rapport |
| `license-compliance` | 4 | SBOM et audit des licences |

## Conformité
| Workflow | Phases | Description |
|----------|--------|-------------|
| `rse-compliance` | 7 | RGPD, AI Act, éco, social, audit éthique |
| `ao-compliance` | 5 | Conformité marchés publics (CCTP/PV) |

## Ops
| Workflow | Phases | Description |
|----------|--------|-------------|
| `cicd-pipeline` | 4 | Mise en place et exécution CI/CD |
| `monitoring-setup` | 5 | Infrastructure de monitoring |
| `chaos-scheduled` | 5 | Chaos engineering |
| `canary-deployment` | 5 | Déploiement progressif 1 % → 10 % → 50 % → 100 % |
| `backup-restore` | 4 | Sauvegarde avec vérification RPO/RTO |

## Données
| Workflow | Phases | Description |
|----------|--------|-------------|
| `data-migration` | 7 | Migration de données avec HITL GO/NOGO |
| `test-data-pipeline` | 4 | Pipeline de génération de données de test |
| `i18n-validation` | 4 | Contrôles d'internationalisation |

## Autres
| Workflow | Phases | Description |
|----------|--------|-------------|
| `iac-pipeline` | 5 | Infrastructure as Code |
| `tech-debt-reduction` | 5 | Réduction de la dette technique |
| `review-cycle` | 2 | Cycle de revue de code |
| `sf-pipeline` | 3 | Pipeline d'auto-amélioration |

[English](Workflows)
