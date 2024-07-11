package com.solvd.pages;

import org.openqa.selenium.By;

import com.codeborne.selenide.Selenide;
import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.Keys;

import static com.codeborne.selenide.Selenide.$;

public class GoogleSearchPage {

    private final SelenideElement searchArea = $(By.xpath("//textarea[contains(@class,'gLFyf')]"));

    public GoogleSearchPage open() {
        Selenide.open("https://www.google.com/");
        return this;
    }

    public GoogleResultPage search(String text) {
        searchArea.sendKeys(text, Keys.ENTER);
        return new GoogleResultPage();
    }
}
