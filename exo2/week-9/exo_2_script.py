#!/usr/bin/env python3.9

from exo_2_register import register
from exo_2_login import login


def main():
    try:
        print("Executing the register function.")
        register("Lucas", "oui.jpg")
        print("Executing the login function.")
        login("Lucas", "oui.jpg")
        print("Executing the login function.")
        login("Lucas", "non.jpeg")
    except Exception:
        raise


if __name__ == "__main__":
    main()
