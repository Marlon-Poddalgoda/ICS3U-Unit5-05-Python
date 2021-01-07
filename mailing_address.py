#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on January 2021
# This program formats a user inputted address to mailing address specs


def mailing(name, srt_num, srt_name, city, province, post_code,
            apt_num=None):
    # This function formats a mailing address

    # process
    mail_address = name
    if apt_num is not None:
        mail_address = (mail_address + "\n" + apt_num + "-" + srt_num +
                        " " + srt_name + "\n" + city + " " + province + "  "
                        + post_code)
    else:
        mail_address = (mail_address + "\n" + srt_num + " " + srt_name +
                        "\n" + city + " " + province + "  " + post_code)

    return mail_address


def main():
    # this function receives input
    print("This program formats your address to a mailing address.")

    # apartment check
    apt_num = None

    # input
    name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_num = input("Enter your apartment number: ")
    srt_num = input("Enter your street number: ")
    srt_name = input("Enter your street name AND type"
                     " (Main St, Express Pkwy...): ")
    city = input("Enter your city: ")
    province = input("Enter your province (as an abbreviation, ex:"
                     " ON, BC...): ")
    post_code = input("Enter your postal code (123 456): ")
    print("")

    # call functions
    if apt_num is not None:
        address = mailing(name.upper(), srt_num.upper(),
                          srt_name.upper(), city.upper(),
                          province.upper(), post_code.upper(),
                          apt_num.upper())
    else:
        address = mailing(name.upper(), srt_num.upper(),
                          srt_name.upper(), city.upper(),
                          province.upper(), post_code.upper())

    # output
    print(address)


if __name__ == "__main__":
    main()
