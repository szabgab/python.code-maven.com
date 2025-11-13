
## TODO

* Write to Excel
* [EDA](https://en.wikipedia.org/wiki/Exploratory_data_analysis)
* Building ML model
* Anomaly detection

We can add repository level instruction for GitHub Copilot to the file `.github/copilot-instructions.md` and those will be taken in account.

* https://dev.to/anchildress1/all-ive-learned-about-github-copilot-instructions-so-far-5bm7
* https://dev.to/anchildress1/everything-i-know-about-github-copilot-instructions-from-zero-to-onboarded-for-real-4nb0

* https://dev.to/deved/build-apps-with-google-ai-studio
* https://dev.to/devteam/announcing-the-first-dev-education-track-build-apps-with-google-ai-studio-ej7

## Mastermind

Let's write a python project: A game bwteeen te computer and the user.
The computer picks 4 digits out the numbers 1-6 and hides them. Order of the digits matter.

The user then tries to find out what are the 4 digits and in which order.
On every turn the user guesses the 4 digits. The computer compares the current guess to the hidden numbers. For every digit that matches in their location the computer displays a * and for every digit that matches, but is in the wrong location the computer displays a + character.
The game is over when the user matched the 4 digits in the right order.
