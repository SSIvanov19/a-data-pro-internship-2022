<div align = "center">
  <img src="https://user-images.githubusercontent.com/63718744/177458019-811db0bb-e8cd-433b-92dc-072b363e23cc.png">
</div>

<div align = "center">
  <img src = "https://img.shields.io/github/languages/count/SSIvanov19/a-data-pro-internship-2022?style=for-the-badge">
  <img src = "https://img.shields.io/github/repo-size/SSIvanov19/a-data-pro-internship-2022?style=for-the-badge">
  <img src = "https://img.shields.io/github/last-commit/SSIvanov19/a-data-pro-internship-2022?style=for-the-badge">
  <img src = "https://img.shields.io/github/languages/top/SSIvanov19/a-data-pro-internship-2022?style=for-the-badge">
</div>

---

<p align = "center" style = "font-size:4em">
  <strong>
    A web application, that shows the most recent news and shows AI generated statistics for them, made in Django  
  </strong>
</p>

---
## About 💻 <a name = "about"></a>
Powered by AI, our project has the goal to provide citizens with quick and easy access to the news that they consider important. They can sort, filter and display statistics for each one of them!

## Demo of our project 🎥 <a name = "demo"></a>
<img src = "https://user-images.githubusercontent.com/63718744/177466392-a3ffdb8e-dd9e-4e08-b98d-907c6e7df8ee.png" alt = "demo img 1">
<img src = "https://user-images.githubusercontent.com/63718744/177466535-95417566-ccf3-4efa-b22c-f24e0cc79865.png" alt = "demo img 2">

## Related documents 📄 <a name = "docs"></a>
   + [Presentation](https://codingburgas-my.sharepoint.com/:p:/g/personal/ssivanov19_codingburgas_bg/EWzyPB3o1GVCusRvMgAC-A4B9bC_zgRfuI8J7IqIQsM7Lg?e=86A2V2)

## Usage 🖱️ <a name = "usage"></a>
Just go to the news page! There you will fimd information for all of the news. You can filter and serch for specific news, if you want!
  
## Installation ⚙ <a name = "installation"></a>

You can start with downloading our project form [GitHub](https://github.com/SSIvanov19/a-data-pro-internship-2022/archive/refs/heads/master.zip) by pressing the **green clone button**

OR

Pasting this line of code in **your favourite Terminal**:

```
git clone --recursive https://github.com/SSIvanov19/a-data-pro-internship-2022.git
```

## Deployment 💻
You can deploy the project with just one line using docker. Just place this line in **your favourite Terminal**:
```
  docker-compose up
```

OR

If you want to deploy manually, first you need to create a **Database**. This can be achieved by pasting the following line in your postgresql server:
```
  CREATE DATABASE textquerydb
```

Then, you need to make a **.env** in the root of the project. You can see [**.env.example**](https://github.com/SSIvanov19/a-data-pro-internship-2022/blob/master/.env.example) for the file in the root folder.

To start the Web App, paste the following lines in **your favourite Terminal**, while you are in the **root** folder:
```
  pip install -r requirements.txt
  python -m spacy download mk_core_news_md
  python manage.py migrate
  python manage.py collectstatic --no-input
  python .\manage.py runserver
```

## Our Team 👨‍💻 <a name = "team"></a>
Stoyan Ivanov | Radoslav Lisitsov | Petar Nikolov | Petar Spasov | Kaloyan Pazlamachev |
-----------------|------------------|----------------|---------------|-----------------------|
*[SSIvanov19](https://github.com/SSIvanov19)* | *[RPLisitsov19](https://github.com/RPLisitsov19)* | *[PRNikolov19](https://github.com/PRNikolov19)* | *[PZSpasov19](https://github.com/PZSpasov19)* | *[KNPazlamachev19](https://github.com/KNPazlamachev19)* |
Web Developer | Front-End Developer | Front-End Developer | Scrum Trainer | QA Engineer |

---

```
Thank you for scrolling this far! Please consider giving the repo a star ⭐.
```
