# ADR-012 : SBOM and supply-chain baseline

- **Statut** : Proposé
- **Date** : 2026-05-24
- **Décideurs** : CTO, CISO, CAIO

## Contexte

Les clients enterprise APAC exigeront de plus en plus une transparence supply-chain (vulnérabilités, licences, dépendances). NIST SSDF SP 800-218 PS.3.2 requiert la production de SBOM pour chaque release.

## Décision

**SBOM obligatoire à chaque release** sur tout projet Architekt (plateforme + projets clients).

### Format

- **CycloneDX JSON** (format primaire)
- **SPDX** (format secondaire pour interop)

### Outils

| Stack | Outil SBOM |
|-------|-----------|
| Python | `cyclonedx-py` + pip-audit |
| Node / TypeScript | `@cyclonedx/cyclonedx-npm` |
| Docker images | Syft (Anchore) |
| Java | `cyclonedx-maven-plugin` ou `cyclonedx-gradle-plugin` |
| Multi-langage | Syft (CI universel) |

### CI workflow

```yaml
sbom:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Generate CycloneDX SBOM
      uses: anchore/sbom-action@v0
      with:
        format: cyclonedx-json
        output-file: sbom-cyclonedx.json
    - uses: actions/upload-artifact@v4
      with: { name: sbom, path: sbom-cyclonedx.json }
```

### Pipeline sécurité additionnel

- **SAST** : Bandit (Python), Semgrep (multi-lang)
- **SCA** : Safety (Python), npm audit, OWASP Dependency-Check
- **Secret scanning** : trufflehog en CI + git pre-commit
- **Signature** : Sigstore (Cosign) pour artefacts release (Phase 5)
- **Pinning** : versions exactes dans lockfiles (pas de `^` ni `~`)

### VEX (Vulnerability Exploitability eXchange)

Pour réduire bruit : statut d'exploitabilité par CVE dans `vex.json` lié à chaque SBOM (Phase 5+).

## Conséquences

### Positives
- Conformité NIST SSDF, CRA EU 2026, exigences clients enterprise
- Visibilité dépendances + vulnérabilités
- Argument vente B2B (rapport sécurité commercialisable, cf. ADR-015)

### Négatives
- Stockage artefacts (mitigable, ~1 MB par SBOM)
- Bruit CVE (mitigation : VEX)
- Coût outils CI (faible, OSS principalement)

## Sources

- NIST SP 800-218 SSDF v1.1 PS.3.2 (févr. 2022)
- NIST SP 800-218 v1.2 IPD (déc. 2025)
- CycloneDX (OWASP)
- SPDX (Linux Foundation)
- NTIA SBOM Minimum Elements
- EU Cyber Resilience Act (CRA) 2024 — applicable 2027
