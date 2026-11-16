# Security log

| Date | Result | Notes |
|------|--------|-------|
| 2026-11-16 | Fixed, 2 items need Omar | Patched composer/npm lockfiles in app, kawader, site, extension and the web-app template (incl. critical Laravel TokenGuard alert); added least-privilege `permissions:` to 10 workflows. Needs Omar: (1) HSTS and X-Content-Type-Options headers missing on all live sites (nginx); (2) Dependabot alerts off on 8 repos; (3) major upgrades pending: asaas/site (shadcn-vue chain, 13 npm findings), core (zod 4), radar (sharp 0.35). No leaked secrets, no exposed internal tools. |
