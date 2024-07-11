package com.solvd.pages;

import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.By;

import static com.codeborne.selenide.Selenide.$;

public class GoogleResultPage {

    private final SelenideElement searchArea = $(By.xpath("//textarea[contains(@name,'q')]"));

    public String getTextInSearchArea() {
        return searchArea.getText();
    }
}
