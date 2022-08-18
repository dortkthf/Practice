-- SQLite
CREATE TABLE health(
    id INTEGER,
    sido INTEGER,
    gender INTEGER,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    waist INTEGER,
    va_left INTEGER,
    va_right INTEGER,
    blood_pressure INTEGER,
    smoking INTEGER,
    is_drinking INTEGER
)

.schema health
.mode csv
.import health.csv health

.mode column

SELECT * FROM health LIMIT 5;

SELECT smoking, COUNT(smoking) FROM health GROUP BY smoking;

SELECT is_drinking, COUNT(is_drinking) FROM health GROUP BY is_drinking;

SELECT is_drinking,COUNT(is_drinking) FROM health WHERE blood_pressure>=200 GROUP BY is_drinking;

SELECT sido,COUNT(sido)
 FROM health GROUP BY sido HAVING COUNT(sido)>=50000;

SELECT height, COUNT(height) 사람수 FROM health GROUP BY height ORDER BY 사람수 DESC LIMIT 5;

SELECT height, weight, COUNT(*) 사람수 FROM health GROUP BY height, weight ORDER BY 사람수 DESC LIMIT 5;

SELECT is_drinking, AVG(waist), COUNT(is_drinking) FROM health GROUP BY is_drinking;

SELECT gender, ROUND(AVG(va_left),2) 평균_왼쪽_시력, ROUND(AVG(va_right),2) 평균_오른쪽_시력 FROM health GROUP BY gender;

SELECT age,AVG(height) 평균_키 ,AVG(weight) 평균_몸무게 FROM health GROUP BY age HAVING AVG(height) >=160 AND AVG(weight) >= 60;

SELECT is_drinking,smoking, AVG(weight)/POWER((AVG(height)*0.01),2) BMI FROM health WHERE is_drinking != '' AND smoking != '' GROUP BY is_drinking, smoking;