[![Nightly builds](https://github.com/LinkedInLearning/recommendation-systems-a-practical-introduction-2703578/actions/workflows/nightly_builds.yml/badge.svg)](https://github.com/LinkedInLearning/recommendation-systems-a-practical-introduction-2703578/actions/workflows/nightly_builds.yml)

# Recommendation Systems: A Practical Introduction
![lil-thumbnail-url]

This is the repository for the LinkedIn Learning course Recommendation Systems: A Practical Introduction. The full course is available for free from [LinkedIn Learning][lil-course-url].

Recommendation systems are among the most profitable Artificial Intelligence solutions you can deploy, for the simple fact that they can understand what people are interested in.  Anytime you buy or browse online, there are probably recommendation systems at work presenting you with options at each step. 

In this free course, [Miguel Fierro](https://www.linkedin.com/in/miguelgfierro/) teaches a practical introduction for building, deploying, and testing recommendation systems. He offers practical, real-world examples to show how you can make a direct impact in your company with recommendation systems. 

Whether you’re a Data Scientist, Machine Learning Engineer, Data Engineer, Software Engineer, or Data Analyst, join Miguel in this course to get started building your first recommendation system.

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/recommendation-systems-a-practical-introduction
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D560DAQG8MPbTpDa58w/learning-public-crop_675_1200/0/1706307294561?e=2147483647&v=beta&t=KdN9SWgdqYQupXRM25E8D4WArQcadJt-JRZh16fgrpE

## Installation via GitHub Codespaces

1. Go to Code.
2. Click on Create codespace on main.
3. After the codespace is ready, you can run all the notebooks.

## Installation in local

```
conda create -n reco Python=3.7
conda activate reco
pip install numpy "Cython<4" "scipy<1.11.0"
pip install -r requirements.txt
```

## Test

To test the code, run the following command:

```
pytest tests
```