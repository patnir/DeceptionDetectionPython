Open-Domain Deception Dataset
=============================================

Veronica Perez-Rosas and Rada Mihalcea
Language and Information Technologies
University of Michigan

vrncapr@umich.edu
mihalcea@umich.edu

Version 1.0
August 2015


1. Introduction

This document describes the dataset used in the paper "Experiments in Open Domain Deception Detection" (Perez-Rosas and Mihalcea, 2015).


2. Dataset information

The dataset contains short open domain truths and lies from 512 users. Seven lies and seven truths are provided for each user. The dataset has a total of 7168 single line sentences, out of which 3598 are truths and 3569 are lies. It also includes user's demographic information, such as gender, age, country of origin, and education level. The dataset was collected via crowdsourcing using Amazon Mechanical Turk. 


3. Dataset structure

The data is presented in comma separated values (CSV) format in the file "7Truth7LiesDataset.csv". Each line of this file represents either a lie or a truth by one user, along with his/her demographic data, and it has the following format:

id,gender,age,education,country,text,class

where:
- id:  instance identifier, indicating user number, and also including the gender, class, and truth/lie sentence (numbered from 1 to 7).
     - Examples:  2_f_l_1 (user 2, female, lie 1)
                  3_m_t_2 (user 3, male, truth 2)
- gender: male or female
- age:  age, ranging between 18-72 years
- education: user education level, including High School, High School Graduate, Some college, no degree, Bachelors degree, Associates degree, Graduate degree (Masters, Doctorate, etc.)
- country: country of origin
- text: a single line sentence containing a short open domain lie or truth
- class: class label, truth or lie

The lines in this file are ordered by the "id" attribute, which is ordered first by user number within gender and then by class.


4. Feedback

For further questions or inquiries about this dataset, you can contact: Veronica Perez-Rosas (vrncapr@umich.edu) or Rada Mihalcea (mihalcea@umich.edu).


5. Citation Information

If you use this dataset, please cite:

@Proceedings{Perez-Rosas15,
author="P{\'e}rez-Rosas, Ver{\'o}nica and Mihalcea, Rada",
title="Experiments in Open Domain Deception Detection",
series="Proceedings of the Conference on Empirical Methods in Natural Language Processing",
year="2015",
location="Lisboa, Portugal",
}


6. Acknowledgements

This material is based in part upon work supported by National Science Foundation awards #1344257 and #1355633, by grant #48503 from the John Templeton Foundation, and by DARPA-BAA-12-47 DEFT grant #12475008.  Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation, the John Templeton Foundation, or the Defense Advanced Research Projects Agency.
