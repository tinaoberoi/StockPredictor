# App for stock prediction using knn classifier model

The App uses knn classifier for predicting if the stock on the next day will go up or down. It uses laps for the 5 lap predictors for the 5 days to make a prediction.

## Project Flow:
![app flow](./project_flow.drawio.png)
## Tech Stack Used:
- This project uses [pipreqs](https://github.com/bndr/pipreqs) for creating requirements.txt
- The Project is deployed on AWS EC2 clusters.
- Github actions are used for deployment on EC2. (.github/workflows)
- Here gunicorn is used to start the server.
- Backend is written in Flask.
- For model creating `numpy, sklearn, pandas` are used.

The app is deployed [here](http://ec2-3-22-236-250.us-east-2.compute.amazonaws.com:5001/)

![png](static/app_preview.png)

Data format to add:

```
Enter the Array laps in the form:
Lap1 Array : 0.381,-0.192,-2.624,-1.055,5.01
Lap2 Array: -0.403,1.392,0.213,0.614,-0.623
Lap3 Array: 0.546,-0.562,0.701,0.68,-0.189
Lap4 Array: -0.841,-0.151,0.359,-1.747,0.546
Lap5 Array: 0.812,-0.218,-0.865,1.183,-1.334
```

After adding laps, based on this data the model returns the up/down indicator.

![](./static/app_result_view.png)

To run locally, use the following commands:

``` shcode
 chmod +x .github/scripts/build.sh
 .github/scripts/build.sh
```

Note: If you are still not in env virtual environment please run
```source env/bin/actiavte```