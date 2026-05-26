# Content-Security-Policy (CSP)

Architekt Platform sets a `Content-Security-Policy` response header on every HTTP response via the `security_headers` middleware in `platform/server.py` (around lines 598–660).

## Middleware

Implementation: `@app.middleware("http")` → `security_headers` in `platform/server.py`.

Other headers set in the same middleware:

- `X-Content-Type-Options: nosniff`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `X-Frame-Options: DENY` (default pages only; omitted on workspace)
- `Strict-Transport-Security` when the request is HTTPS

## Two policies

| Variant | Path match | Why |
|---------|------------|-----|
| **Default** | All routes except workspace | Standard UI: Chart.js CDN, Google Fonts, Dicebear avatars |
| **Workspace** | `/projects/{id}/workspace` | Embedded previews (iframe): localhost ports, broader `img-src` / `frame-src` |

### Default CSP

```
default-src 'self';
script-src 'self' ['nonce-…'] 'unsafe-inline' 'unsafe-eval' https://unpkg.com https://cdn.jsdelivr.net;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
font-src 'self' https://fonts.gstatic.com;
img-src 'self' data: https://api.dicebear.com https://avatars.githubusercontent.com;
connect-src 'self';
frame-ancestors 'none'
```

Plus `X-Frame-Options: DENY`.

### Workspace CSP

```
default-src 'self';
script-src 'self' ['nonce-…'] 'unsafe-inline' 'unsafe-eval';
style-src 'self' 'unsafe-inline';
font-src 'self' data:;
img-src 'self' data: blob: https:;
connect-src 'self';
frame-src 'self' http://localhost:* http://127.0.0.1:* https:;
frame-ancestors 'none'
```

No `X-Frame-Options` (iframes are required for preview tooling).

## `unsafe-inline` today

Both policies keep `'unsafe-inline'` and `'unsafe-eval'` on `script-src` because:

- HTMX uses inline attributes and dynamic script injection patterns across many templates.
- Some pages load inline bootstrapping without external bundles.
- Chart.js / legacy snippets may rely on eval in dev tooling.

Jinja2 auto-escaping and `connect-src 'self'` limit XSS impact; CSP is defense-in-depth, not the only control.

## Optional nonce (`PLATFORM_CSP_NONCE`)

| Env | Config | Default |
|-----|--------|---------|
| `PLATFORM_CSP_NONCE=0` | `ServerConfig.csp_nonce = False` | **off** |
| `PLATFORM_CSP_NONCE=1` | `ServerConfig.csp_nonce = True` | per-request nonce |

When enabled:

1. Middleware generates `secrets.token_urlsafe(16)` **before** `call_next` (so templates can read it during render).
2. `script-src` gains `'nonce-{value}'` alongside existing sources (including `'unsafe-inline'` for HTMX compatibility).
3. `request.state.csp_nonce` is set for Jinja (`{{ request.state.csp_nonce }}` on `<script nonce="…">`).

Documented in `platform/config.py` (`ServerConfig.csp_nonce`) and `load_config()` env override.

**Local trial:**

```bash
PLATFORM_CSP_NONCE=1 python3 -m uvicorn platform.server:app --host 0.0.0.0 --port 8099 --ws none
```

## Roadmap: remove `unsafe-inline`

Target end state (security-frontend-dev skill alignment):

| Phase | Work |
|-------|------|
| 1 | Enable `PLATFORM_CSP_NONCE=1` in staging; tag all first-party `<script>` in `base.html` and shared partials with `nonce="{{ request.state.csp_nonce }}"` |
| 2 | Move inline `<script>` blocks to `/static/js/*.js` or `type="module"` with nonce |
| 3 | Audit HTMX `hx-on::*` and inline handlers; replace with `htmx.config` / external listeners where possible |
| 4 | Drop `'unsafe-eval'` when no dependency requires it |
| 5 | Remove `'unsafe-inline'` from `script-src`; keep `'unsafe-inline'` on `style-src` only if needed for critical CSS |
| 6 | Add CSP violation reporting (`report-uri` / `report-to`) and Playwright smoke asserting no console CSP errors |

Until phase 5, production should remain on `PLATFORM_CSP_NONCE=0` unless templates are fully nonce-tagged.

## Related docs

- `docs/architekt/PLATFORM-BACKLOG.md` — Wave 7 security polish
- `docs/architekt/ROADMAP-WAVE7.md` — P2 scale items
- `docs/wiki/Security.md` — adversarial L0–L2 overview
