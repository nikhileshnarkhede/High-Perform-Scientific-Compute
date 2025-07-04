This project is about the classification of music into genres by NIKHILESH NARKHEDE (02196141)


Project Structure

Final Project
|
|--- Data
|    |--- Convert_Audio_File_to_jpg_file (Generated my spectrogram creator)
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
|    |     |--- genres_train_val_split_data
|    |     |--- Music_Genre_Identification_With_1_Core.ipynb
|    |        .
|    |        .
|    |        .
|    |        .
|    |--- WORKER 8
|    |--- core_data.txt
|    |--- DV of Exp with Core for Deep Learning Model Training.ipynb
|
|--- PREPROCESSING WITH HPSC
|    |--- Convert_Audio_File_into_jpg_file_using_spectrogram.ipynb
|    |--- Convert_Audio_File_into_jpg_file_using_spectrogram_with_multiple_worker.ipynb
|
|--- Final Project.pdf
|--- Final Project.pptx


Note: 
	While working on this project I saved the "Final Project" folder at Desktop. So all the paths in the Jupyter Notebook will start with "C:\Users\nikhi\OneDrive\Desktop\". Please change accordingly. 

	in 
	|--- DEEP LEARNING WITH HPSC
	|    |--- WORKER 1
	|    |     |--- genres_train_val_split_data
	|    |     |--- Music_Genre_Identification_With_1_Core.ipynb 

	I have written the function append_core_data which takes two parameters number of workers and Execution time for training using time.time() from time Library. And save this information at "C:\Users\nikhi\OneDrive\Desktop\Final Project\DEEP LEARNING WITH HPSC	\core_data.txt". Forward the DV of Exp with Core for Deep Learning Model Training.ipynb pulls the data for plotting the graph. 


IMP Note: 

	This is done for all the workers from 1 to 8. And saved in core_data.txt row-wise. 
	
	Formula used:-

		Speed-up = Execution Time (Sequential) / Execution Time (Parallel)

		Efficiency = Speed-up / Number of Workers

	Conceptually Efficiency range from [0,1]. But in the background, there might be many other tasks running which might affect the Execution time of the model training task. Please consider it when you consider the graph.     

​



