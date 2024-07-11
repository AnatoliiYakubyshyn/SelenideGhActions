import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.codeborne.selenide.Configuration;

import com.solvd.pages.GoogleSearchPage;

public class GoogleSearchTest {


    @BeforeClass
    public void setUp() {
        Configuration.remote ="http://localhost:4445/wd/hub";
        Configuration.timeout = 10000;
        Configuration.browser = "chrome";
        Configuration.browserVersion = "125";
    }

    @Test
    public void test() {
        String input = "hello";
        GoogleSearchPage googleSearchPage = new GoogleSearchPage();
        Assert.assertEquals(googleSearchPage.open().search(input).
                getTextInSearchArea(), input);
    }
}
