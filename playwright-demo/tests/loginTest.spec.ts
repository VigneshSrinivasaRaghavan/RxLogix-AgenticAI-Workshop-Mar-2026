import { test} from '@playwright/test';
import { AdminPage } from './pages/adminPage';
import { DashboardPage } from './pages/dashboardPage';
import { LoginPage } from './pages/loginPage';
import * as orangeHrmData from './testData/orangeHrmLoginData.json';

test('Login test with valid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const dashboardPage = new DashboardPage(page);
    const adminPage = new AdminPage(page);

    await loginPage.b_navigateTo('https://opensource-demo.orangehrmlive.com/');
    await loginPage.enterUsername(orangeHrmData.validUsername);
    await loginPage.enterPassword(orangeHrmData.validPassword);
    await loginPage.clickLogin();

    await dashboardPage.clickAdminTab();
    await adminPage.enterUserName(orangeHrmData.validUsername);
    await adminPage.clickSearch();

    await dashboardPage.clickProfileAccordion();
    await dashboardPage.clickLogout();
});