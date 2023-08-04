# correlation
[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)

correlation tries to use machine learning to help assess relations between data in testing/bug hunting

== Installing ==

To install camml, simply extract the BI-CaMML.zip file to a folder of your choice.

You will need to make sure you have at least Java 6, and that the "java" program is in your system's PATH variable. (Java will normally do this for you automatically.)

== Running CaMML with a GUI ==

== CaMML GUI ==

CaMML has a stand-alone Java-based GUI (added 02/2013) that should be suitable for
most basic learning tasks. The GUI has a data viewer, basic network viewer (based
on Netica libraries), and support for learning DBNs.

- To run the GUI, go to the BI-CaMML directory and use:
  > camml_gui.sh
  > camml_gui.bat (Windows)

At present, this GUI only supports data files that are discrete and contain no
missing values.

== CaMML command line (and Weka Wrapper) ==

CaMML can be used from the command line, by default as a standard weka classifier.
It can also be added to the weka GUI, but that's beyond the scope of this doc.

- To get a list of options, go to the BI-CaMML directory and use:
  > camml.sh
  > camml.bat (Windows)

- To train/test a model using weka's default x-fold validation, use:
  > camml.sh -t Camml/camml/test/iris.arff
  > camml.bat -t Camml/camml/test/iris.arff (Windows)




== Practical Example ==

- prepare the csv files (vulnerabilities.csv) 
- Convert continuous values to discrete ones(e.g. instead of '189.5', '89.8' use 'big', 'small' )
  python3 Continuous2Discrete.py
- launch camml_gui.sh
- load the csv file with discrete valued
- Go to 'Run' tab and press 'Run CaMML' 
- Go to 'Results' and select a network and press 'View Selected Network'

![Sample](sample.png?raw=true "Sample")

