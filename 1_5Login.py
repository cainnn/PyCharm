from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://47.116.12.183/index.html")
    page.get_by_placeholder("请输入用户名").click()
    page.get_by_placeholder("请输入用户名").fill("dpblue")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").fill("unixware")
    page.get_by_role("button", name="立即登录 >").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
