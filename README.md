# Web Application LegalBERT-th (Prototype)

#### WEB APPLICATION 
- > [click!](http://52.230.5.114:5007/) And you can read [Manual](https://drive.google.com/file/d/1fuuNNpR5_o1d3h0yKLFHNHjkpAhhL7Lx/view?usp=sharing)

This is Web Application for LegalBERT-th project : Development of Legal Q&A Dataset and Automatic Question Tagging.
Web Application compatible with [API (LegalBERT-th)](https://github.com/WiratchawaKannika/API_LegalBERT-th). We used Python with HTML, css to create Web Application. For Identifying Type of Law of Post in Legal Webboards and display the top 3 questions and answers close to the new questions when user ask questions about Thai Legal.

## requirements

```shell
- Python == 3.7+
```

### Installation

```shell
- pip install pandas
- pip install Flask
```

### Run Web Application 
Open your terminal

First, you have to run Database file. Consist 2 file : (1) Data_similarity.py (2) Data.py

```shell
- python Data_similarity.py
```

```shell
- python Data.py
```

The second. You run Web Application file : main_run.py 
```shell
- python main_run.py
```

And you run Web Application file for Admin page : admin_run.py 
```shell
- python admin_run.py
```

You will get URL, for example : ```http://127.0.0.1:5000/ ```  
Copy and paste in your Web Browser.


#### WebPage detail of LegalBERT-th Project
- [here!](https://github.com/WiratchawaKannika/LegalDoc_NLP) 
- [Web Project!](https://wiratchawakannika.github.io/LegalDoc_NLP/)

#### GitHub my Project (LegalBERT-th model)
- [here!](https://github.com/WiratchawaKannika/bert/tree/master/LegalBERT-th) 

#### GitHub my Project (Code scraping data: Thai law, Dataset Development)
- [here!](https://github.com/WiratchawaKannika/LegalDoc_project4)
