This project is about the classification of music into genres by NIKHILESH NARKHEDE (02196141)





Project Structure



Final Project

|

|--- Data

|    |--- Convert\_Audio\_File\_to\_jpg\_file (Generated my spectrogram creator)

|    |--- genres

|          |--- blues

|          |--- classical

|          |--- country

|          |--- disco

|          |--- hiphop

|          |--- jazz

|          |--- metal

|          |--- pop

|          |--- reggae

|          |--- rock

|

|--- DEEP LEARNING WITH HPSC

|    |--- WORKER 1

|    |     |--- genres\_train\_val\_split\_data

|    |     |--- Music\_Genre\_Identification\_With\_1\_Core.ipynb

|    |        .

|    |        .

|    |        .

|    |        .

|    |--- WORKER 8

|    |--- core\_data.txt

|    |--- DV of Exp with Core for Deep Learning Model Training.ipynb

|

|--- PREPROCESSING WITH HPSC

|    |--- Convert\_Audio\_File\_into\_jpg\_file\_using\_spectrogram.ipynb

|    |--- Convert\_Audio\_File\_into\_jpg\_file\_using\_spectrogram\_with\_multiple\_worker.ipynb

|

|--- Final Project.pdf

|--- Final Project.pptx





Note: 

&nbsp;	While working on this project I saved the "Final Project" folder at Desktop. So all the paths in the Jupyter Notebook will start with "C:\\Users\\nikhi\\OneDrive\\Desktop\\". Please change accordingly. 



&nbsp;	in 

&nbsp;	|--- DEEP LEARNING WITH HPSC

&nbsp;	|    |--- WORKER 1

&nbsp;	|    |     |--- genres\_train\_val\_split\_data

&nbsp;	|    |     |--- Music\_Genre\_Identification\_With\_1\_Core.ipynb 



&nbsp;	I have written the function append\_core\_data which takes two parameters number of workers and Execution time for training using time.time() from time Library. And save this information at "C:\\Users\\nikhi\\OneDrive\\Desktop\\Final Project\\DEEP LEARNING WITH HPSC	\\core\_data.txt". Forward the DV of Exp with Core for Deep Learning Model Training.ipynb pulls the data for plotting the graph. 





IMP Note: 



&nbsp;	This is done for all the workers from 1 to 8. And saved in core\_data.txt row-wise. 

&nbsp;	

&nbsp;	Formula used:-



&nbsp;		Speed-up = Execution Time (Sequential) / Execution Time (Parallel)



&nbsp;		Efficiency = Speed-up / Number of Workers



&nbsp;	Conceptually Efficiency range from \[0,1]. But in the background, there might be many other tasks running which might affect the Execution time of the model training task. Please consider it when you consider the graph.     



​







This project is about the classification of music into genres by NIKHILESH NARKHEDE (02196141)





Project Structure



Final Project

|

|--- Data

|    |--- Convert\_Audio\_File\_to\_jpg\_file (Generated my spectrogram creator)

|    |--- genres

|          |--- blues

|          |--- classical

|          |--- country

|          |--- disco

|          |--- hiphop

|          |--- jazz

|          |--- metal

|          |--- pop

|          |--- reggae

|          |--- rock

|

|--- DEEP LEARNING WITH HPSC

|    |--- WORKER 1

|    |     |--- genres\_train\_val\_split\_data

|    |     |--- Music\_Genre\_Identification\_With\_1\_Core.ipynb

|    |        .

|    |        .

|    |        .

|    |        .

|    |--- WORKER 8

|    |--- core\_data.txt

|    |--- DV of Exp with Core for Deep Learning Model Training.ipynb

|

|--- PREPROCESSING WITH HPSC

|    |--- Convert\_Audio\_File\_into\_jpg\_file\_using\_spectrogram.ipynb

|    |--- Convert\_Audio\_File\_into\_jpg\_file\_using\_spectrogram\_with\_multiple\_worker.ipynb

|

|--- Final Project.pdf

|--- Final Project.pptx





Note: 

&nbsp;	While working on this project I saved the "Final Project" folder at Desktop. So all the paths in the Jupyter Notebook will start with "C:\\Users\\nikhi\\OneDrive\\Desktop\\". Please change accordingly. 



&nbsp;	in 

&nbsp;	|--- DEEP LEARNING WITH HPSC

&nbsp;	|    |--- WORKER 1

&nbsp;	|    |     |--- genres\_train\_val\_split\_data

&nbsp;	|    |     |--- Music\_Genre\_Identification\_With\_1\_Core.ipynb 



&nbsp;	I have written the function append\_core\_data which takes two parameters number of workers and Execution time for training using time.time() from time Library. And save this information at "C:\\Users\\nikhi\\OneDrive\\Desktop\\Final Project\\DEEP LEARNING WITH HPSC	\\core\_data.txt". Forward the DV of Exp with Core for Deep Learning Model Training.ipynb pulls the data for plotting the graph. 





IMP Note: 



&nbsp;	This is done for all the workers from 1 to 8. And saved in core\_data.txt row-wise. 

&nbsp;	

&nbsp;	Formula used:-



&nbsp;		Speed-up = Execution Time (Sequential) / Execution Time (Parallel)



&nbsp;		Efficiency = Speed-up / Number of Workers



&nbsp;	Conceptually Efficiency range from \[0,1]. But in the background, there might be many other tasks running which might affect the Execution time of the model training task. Please consider it when you consider the graph.     



​









