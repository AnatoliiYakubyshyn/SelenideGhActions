import com.codeborne.selenide.Configuration;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.solvd.pages.GoogleSearchPage;

public class GoogleSearchTest {


    @BeforeClass
    public void setup() {
        Configuration.timeout = 1000;
    }

    @Test
    public void test() {
        String input = "hello";
        GoogleSearchPage googleSearchPage = new GoogleSearchPage();
        Assert.assertEquals(googleSearchPage.open().search(input).
                getTextInSearchArea(), input);
    }
}
