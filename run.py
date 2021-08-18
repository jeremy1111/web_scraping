import main_code

if __name__ == '__main__':

    # go to google
    google_url = 'https://www.google.com/'
    main_code.go_to_url(google_url)

    # click agree button
    agree_terms_button = 'L2AGLb'
    main_code.click_button(agree_terms_button)

    # insert query and search
    query_string = 'How to data engineering'
    query_box = 'q'
    input_element = main_code.insert_query_to_box(query_string, query_box)
    main_code.press_enter(input_element)

    # get resulting links
    links_to_scrape = '.yuRUbf [href]'
    links_list = main_code.get_links_list(links_to_scrape)

    # go into the first 5 links
    num_links = 5
    first_five_links = links_list[:num_links]
    count = 1
    for link in first_five_links:
        html_text = main_code.get_text_in_link(link)
        soup_text = main_code.apply_beautifulsoup(html_text)
        filename = "link_text_{}.html".format(count)
        main_code.write_to_file(filename, soup_text)
        count += 1
