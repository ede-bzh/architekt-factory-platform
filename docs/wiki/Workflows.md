# Workflows (41 Built-in)

Each workflow defines a sequence of phases executed by specialized agents. Builtin templates are loaded from `platform/workflows/builtins.py` and YAML under `platform/workflows/templates/`.

## Lifecycle
| Workflow | Phases | Description |
|----------|--------|-------------|
| `product-lifecycle` | 11 | Full product delivery (ideation → deploy → TMA) |
| `feature-sprint` | 5 | Sprint-scoped feature implementation |
| `feature-request` | 6 | Feature request processing |

## DSI
| Workflow | Phases | Description |
|----------|--------|-------------|
| `dsi-platform-features` | 9 | Platform feature development |
| `dsi-platform-tma` | 6 | Platform maintenance |

## Security
| Workflow | Phases | Description |
|----------|--------|-------------|
| `security-hacking` | 8 | Full security audit (recon → exploit → report) |
| `sast-continuous` | 4 | Continuous static analysis |

## TMA (Maintenance)
| Workflow | Phases | Description |
|----------|--------|-------------|
| `tma-maintenance` | 4 | Standard maintenance cycle |
| `tma-autoheal` | 4 | Auto-healing operations |

## SAFe
| Workflow | Phases | Description |
|----------|--------|-------------|
| `pi-planning` | 5 | Program Increment planning |
| `epic-decompose` | 5 | Epic → Feature → Story decomposition |

## Mobile
| Workflow | Phases | Description |
|----------|--------|-------------|
| `mobile-ios-epic` | 5 | iOS epic delivery |
| `mobile-android-epic` | 5 | Android epic delivery |

## Quality
| Workflow | Phases | Description |
|----------|--------|-------------|
| `documentation-pipeline` | 6 | API docs → ADR → changelog → user docs |
| `performance-testing` | 5 | k6 load → analysis → fix loop → report |
| `license-compliance` | 4 | SBOM and license audit |

## Compliance
| Workflow | Phases | Description |
|----------|--------|-------------|
| `rse-compliance` | 7 | GDPR, AI Act, eco, social, ethical audit |
| `ao-compliance` | 5 | Procurement compliance (CCTP/PV) |

## Ops
| Workflow | Phases | Description |
|----------|--------|-------------|
| `cicd-pipeline` | 4 | CI/CD setup and execution |
| `monitoring-setup` | 5 | Monitoring infrastructure |
| `chaos-scheduled` | 5 | Chaos engineering |
| `canary-deployment` | 5 | 1% → 10% → 50% → 100% rollout |
| `backup-restore` | 4 | Backup with RPO/RTO verification |

## Data
| Workflow | Phases | Description |
|----------|--------|-------------|
| `data-migration` | 7 | Data migration with HITL GO/NOGO |
| `test-data-pipeline` | 4 | Test data generation pipeline |
| `i18n-validation` | 4 | Internationalization checks |

## Other
| Workflow | Phases | Description |
|----------|--------|-------------|
| `iac-pipeline` | 5 | Infrastructure as Code |
| `tech-debt-reduction` | 5 | Technical debt cleanup |
| `review-cycle` | 2 | Code review cycle |
| `sf-pipeline` | 3 | Self-improvement pipeline |

## 🇫🇷 [Workflows (FR)](Workflows‐FR) · 🇪🇸 [ES](Workflows‐ES)
