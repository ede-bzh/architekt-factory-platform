import { test, expect } from "@playwright/test";

const SUPPORTED = ["en", "fr"] as const;
const UNSUPPORTED = ["zh", "de"] as const;

test.describe("Language switching (EN/FR only)", () => {
  for (const lang of SUPPORTED) {
    test(`loads in ${lang}`, async ({ page, context }) => {
      const baseURL = process.env.BASE_URL || "http://localhost:8090";
      await context.addCookies([
        { name: "sf_lang", value: lang, url: baseURL },
      ]);
      await page.goto("/");
      expect(await page.title()).toBeTruthy();
      const content = await page.textContent("body");
      expect(content!.length).toBeGreaterThan(100);
    });
  }

  for (const lang of UNSUPPORTED) {
    test(`unsupported cookie ${lang} still loads (fallback en)`, async ({
      page,
      context,
    }) => {
      const baseURL = process.env.BASE_URL || "http://localhost:8090";
      await context.addCookies([
        { name: "sf_lang", value: lang, url: baseURL },
      ]);
      await page.goto("/");
      expect(await page.title()).toBeTruthy();
    });
  }

  test("locale API returns translations for en and fr", async ({ request }) => {
    for (const lang of SUPPORTED) {
      const response = await request.get(`/api/i18n/${lang}.json`);
      expect(response.status()).toBe(200);
      const data = await response.json();
      expect(Object.keys(data).length).toBeGreaterThan(30);
    }
  });

  test("unsupported locale API falls back to English catalog", async ({
    request,
  }) => {
    const en = await request.get("/api/i18n/en.json");
    const zh = await request.get("/api/i18n/zh.json");
    expect(en.status()).toBe(200);
    expect(zh.status()).toBe(200);
    expect(await zh.json()).toEqual(await en.json());
  });
});
