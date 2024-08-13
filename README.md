# PRED AHCP

PredAHCP employs Random Forest (RF) model to predict anti-hepatitis C peptides (AHCPs) based on sequence features. The model is made available through Pred-AHCP web server: http://tinyurl.com/web-Pred-AHCP.

The RF model harnesses the amino acid sequence of a peptide to predict its potential as an anti-HepC (AHC) agent. Specifically, features were computed based on sequence and physicochemical properties. Feature selection was performed utilizing a combined scheme of mutual information and variance inflation factor. This facilitated the removal of redundant and multicollinear features from the sequence data, enhancing the model’s generalizability in predicting AHCPs. The RF model has an accuracy of about 90%. This resource facilitates the prediction of AHCPs for designing peptide-based therapeutics while also proposing an exploration of similar strategies for designing peptide inhibitors effective against other viruses.

## Methodology

The methodology used in this paper can be described using the following key steps:

### 1. Dataset

- Curated dataset of 326 peptide sequences with known anti-Hepatitis C virus (HCV) activity from the AVPdb repository.
- Created a balanced negative dataset of 326 non-AHCP bioactive peptides.
- Developed an independent validation set of 18 sequences.


### 2. Feature Extraction

- Computed four groups of features: Amino Acid Composition (AAC), Enhanced Amino Acid Composition (EAAC), Composition of k-spaced Amino Acid Pairs (CKSAAP), and CTD encoding (Composition, Transition, Distribution).
- These features capture global and local attributes of peptide sequences.


### 3. Feature Selection

- Used a two-fold strategy combining Mutual Information (MI) and Variance Inflation Factor (VIF).
- MI was used to identify relevant features, calculated 500 times and averaged.
- VIF was then applied iteratively to remove multicollinear features.
- This process was repeated 10 times to improve feature coverage, resulting in 104 relevant features.


### 4. Machine Learning Model Development

- Implemented several classical ML algorithms: Random Forest, Logistic Regression, Support Vector Machine (with different kernels), and Gaussian Naive Bayes.
- Trained and evaluated these models using the selected features.


### 5. Model Evaluation

- Used various performance metrics including accuracy, precision, recall, specificity, AUROC, and Matthews Correlation Coefficient (MCC).
- Tested models on both a test dataset (20% of original data) and the independent validation dataset.


### 6. Web Server Development

- Deployed the best-performing model (Random Forest) as a web server.
- Used Flask for the backend, with Pandas and Scikit-learn for data processing and model implementation.


## Getting Started

### Prerequisites

_Python_ - Download and install Python from https://www.python.org

_Flask_ - Download and install Flask from https://flask.palletsprojects.com/en/3.0.x/

_HTML_ - HTML Docs https://developer.mozilla.org/en-US/docs/Web/HTML

_CSS_ - CSS Docs https://developer.mozilla.org/en-US/docs/Web/CSS

### Installing

1. Clone the repository

```
git clone https://github.com/
```

2. Install the requirements

```
pip install -r requirements.txt
```

3. Move to the Server Directory
```
cd "directory path"
```

4. Start the server
```
flask run
```

5. Open http://localhost:3000 in your browser

## Built With

- [Python](https://www.python.org) - Scripting Language
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Web framework for Python
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Markup language for creating web pages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Styling language for web pages



## Functionalities

- Feature extraction
- Feature selection
- Machine Learning model development
- Web server development

## Folder Structure

```
.
├── index.js
├── Views
│   ├── Auth
│   ├── cart
│   ├── checkout
│   ├── fav
│   ├── orderHistory
│   ├── partials
│   ├── products
│   └── home.ejs
├── Utils
│   └── catchAsync.js
├── controllers
│   └── users.js
├── models
│   ├── cart.js
│   ├── order.js
│   ├── store.js
│   └── user.js
├── package.json
├── package-lock.json
├── public
│   ├── css
│   │   ├── base.css
│   │   ├── cart.css
│   │   ├── checkout.css
│   │   ├── home.css
│   │   ├── login.css
│   │   ├── new.css
│   │   ├── orderHistory.css
│   │   ├── show.css
│   │   ├── signUp.css
│   │   └── stars.css
│   ├── images
│   │   ├── banner.png
│   │   ├── login.jpg
│   │   ├── logo.png
│   │   ├── shopping-bag.png
│   │   └── signup.png
│   └── js
│       ├── formValidation.js
│       └── orderHistory.js
├── middleware.js
├── README.md
├── Demo
│   ├── cart.js
│   ├── order.js
│   ├── store.js
│   └── user.js
├── routes
│   ├── cart.js
│   ├── checkout.js
│   ├── fav.js
│   ├── login.js
│   ├── logout.js
│   ├── orderHistory.js
│   ├── products.js
│   └── products.js

```

## Demo

### Home Page

![Home Page]()


## Manuscript link

https://www.biorxiv.org/content/10.1101/2024.05.05.592323v1

## Contact of all the authors

- Akash Saraswat
- Utsav Sharma
- Aryan Gandotra
- Lakshit Wasan
- Sainithin Artham
- Arijit Maitra
- Bipin Singh

## Code Maintainers

- [Aryan Gandotra](https://github.com/AryanGandotra)
- [Lakshit Wasan](https://github.com/lakshitwasan)

## Contribution

1. Contributions are welcome! Please feel free to submit a Pull Request.
2. Please create an issue for any new feature requests/bugs.
3. Pull requests will be merged after being reviewed.
