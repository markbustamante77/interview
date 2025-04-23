from playwright.sync_api import sync_playwright, expect


def test_run():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

        years = ['2014', '2015']
        for year in years:
            # click 2015 link
            page.locator(f'@id="{year}"').click()
            if year == "2015":
                # get best picture
                best_picture_2015 = page.locator('//i[@class="glyphicon glyphicon-flag"]'
                                            '//ancestor::tr//child::td[@class="film-title"]')
                most_nominations_2015 = page.query_selector_all('//td[@class="film-nominations"]')
                nominations_list = [elem.inner_text() for elem in most_nominations_2015]
                numb_sorted = sorted([nom for nom in nominations_list])
                # find element that correlates with item of number_sorted list
                expect page.locator().some_movie_with_most_noms_15 = numb_sorted[0]

            else:
                # get best picture
                best_picture_2014 = page.locator('//i[@class="glyphicon glyphicon-flag"]'
                                                 '//ancestor::tr//child::td[@class="film-title"]')
                most_nominations_2014 = page.locator('//td[@class="film-nominations"]').all()

                nominations_list = [elem.inner_text() for elem in most_nominations_2014]
                numb_sorted = sorted([nom for nom in nominations_list])
                # find element that correlates with item of number_sorted list
                some_movie_with_most_noms_14 = numb_sorted[0]
                assert

            return best_picture_2014, some_movie_with_most_noms_14, best_picture_2015, some_movie_with_most_noms_14




