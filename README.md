# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)
Bar Lehmann - Project


EEG/GSR Wellness Tracker:

Program goal: Package to facilitate (1) easy gathering of biometric (Electro-encephalogram (EEG) and Galvanic Skin Response (GSR)) data alongside respective subjective reports of ‘mood’ and ‘focus’ and (2) to allow for easy statistical evaluation of associations or correlations between the subjective reports and the biometric data.

What Present Modules Do / Are Meant For
The problem that this program attempts to solve is to aid in EEG data gathering and analysis to easily track and analyze EEG data related to changes in states of ‘Focus’ or ‘Mood’. It is a package aimed to assist students, citizen scientists, neurofeedback practitioners, but might be used by others with similar aims as well. 
Towards these aims, this package module ‘append_table’ first helps to extract relevant amplitude metrics from recordsings of EEG (such as EDF files) and input these metrics into an excel sheet. The excel sheet organizes each recording by a row with its respective amplitude data (in uV). The excel sheet may include other relevant features such as the subjective likert-scale ratings of ‘mood’ and ‘focus’ provided by the user, the name if the individual whose biometrics are being evaluated, the 10-20 site (sensor location on user’s head based on the international 10-20 system), date and time stamps for the recording, and any other relevant information to a recording (the excel sheet columns can be edited based on interest of users). This flexible and rich dataset and interface is the basis for easy streamlining of data recording and later its analysis. 
Other modules in the package such as the ‘graph’ module simplify and quicken the use of MNE-Python (Python API specialized for EEG analyses) to examine data in regards to amplitude data at different electrode sites together or separately, with ability to differentiate by frequencies of interest, or time-frequency diagrams for a user-specified sensor/electrode. 
The ‘eeg_statistics’ module is used for conducting a set of basic analysis such as scatterplots or pearson correlation analyses (for example, to explore connections between perceived ‘mood’ and changes in total amplitude at a particular sensor location). This tool allows the user to specify the columns/variables they would like to compare in an easy-to-use manner to obtain quick basic metrics on their data. 

Overarching Aims of Package
The analyses of this tool/program (such as amplitude-frequency analyses) are highly relevant to those who are tracking EEG or GSR biometrics – an area that has shown great promise in recent neurobiological research. This program is meant for basic wellness tracking / quantified self science. Obviously, this program would not be used for any medical purposes during the timeline of this class as this would require extensive testing and verification, but all efforts will be taken to make it useful in this effort and also to test its validity in its analysis. This program will serve as an initial platform to build more improved and specialized tools for easily and cheaply tracking and analyzing EEG data. 
Presently available and well-known tools for tracking biometrics (such as the Apple Watch, HeartMath biofeedback, Oura Ring, Muse headset) are often very cumbersome and totally inflexible in regards to affording users ease for comparison between a range of biometrics of interest, the variables they consider. They are specialized commercial products often promising to teach “meditation” or some type of “relaxation training” with meager abilities to verify whether the user even feels themselves to be benefitting. Quantified-Self tools such as this are vital to those who actually care to track biometrics around ‘mood’ and ‘focus’ in a more rigorous fashion and of course do so affordably, and in a community of others sharing this interest. This eventual aim is to create a larger community of quantified-self hobbyists and/or citizen scientists a software environment allowing non-technically-inclined individuals a way to rigorously track EEG and GSR metrics in regards to mental wellness report, comparing their own metrics with those of others in similar or different population categories.  

Future Versions of the EEG/GSR Wellness Tracker
The uses of this tool are many and flexible, and later versions will expand upon it’s present use to allow for a more expanded set of metrics to be gathered, and more varied statistics to easily analyze the data. A proximate version will introduce entropy measures that will be extracted, as this metric has shown much promise in research around ‘focus’ and differentiating conscious from unconscious states in anesthesia. Though presently, much of the data such as GSR (galvanic skin response) must be entered manually, future editions will automate this. Specialized testing modules will be developed to rigorously compare baseline with non-baseline recordings of human EEG or neurofeedback-sessions. This package will soon be customized for ease of use at a home setting so that a user can easily take relevant sensors on and off (such as when using the computer for work) and at the click of a button take a recording, and then continue working with very minimal interruptions. De-artifacting of the EEG data will also occur in proximate versions to further streamline obtaining and analyzing the data. 


MNE and the EEG/GSR Wellness Tracker
This package uses MNE: EEG Analysis and Visualization for Python. The use of MNE for this package can be summarized in two components (1) Preprocessing, and (2) Analysis/Visualization that each have a number of components to them. The program would be specialized to interpreting ‘.edf’ file formats. More specifically, the use of MNE for this package is for: 
1)	Preprocessing
Parsing/Cleaning the file
-	“Epoching” or parsing the data into a time-segments that are readable, appropriate for a given analysis to be done
-	Artifact (noise in the signal) identification and suppression
•	Marking bad channels
•	Independent component analysis technique to identify and also to eliminate the “artifacts” (noise in the signal)
2)	Visualization and Analysis 
-	Much of the analysis will be concerned with analyzing amplitude statistics for electrodes separately or in conjunction, comparing this for different wavebands and sensor locations. 
-	Changing montages for EEG recordings (“montages” refer to different means of interpreting the recorded data from sensors via different calculations)
-	Filtering the data through high, low, and notch filters to allow for different lenses into the data.
