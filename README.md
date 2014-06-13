config-demo
===========

Basic configuration of OpenLMIS demo.


To initialize:

1.  Start from a clean OpenLMIS installation
2.  Run """python generateSeed.py""" to create the """seed.sql""" file which will copy the data from the first set of CSVs into the database.
3.  Load the database seed with a command such as """psql open_lmis -f seed.sql"""
4.  Start the OpenLMIS application and login through the web using an admin account with upload rights.
5.  Load each file in the """upload/""" directory in order using the prepended number, e.g. """01_some_file.csv""", with the OpenLMIS Upload feature.
