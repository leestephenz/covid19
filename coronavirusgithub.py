##Stephen Lee 
##July 26, 2020

import pandas as pd
import numpy as np

#Reading in the Indication File into a List of Tuples, then Narrowing down to the Columns Required in a Tuple

with open('INDI20Q1.txt') as fileIndication:
	indicationTupleList = [tuple(map(str, i.split('$'))) for i in fileIndication]
indication = []
for entryIndicationPrimaryID in indicationTupleList:
	indication.append((entryIndicationPrimaryID[0], entryIndicationPrimaryID[3]))
fileIndication.close()

#Reading in the Drug File into a List of Tuples, then Narrowing down to the Columns Required in a Tuple

with open('DRUG20Q1.txt') as fileDrug:
	drugTupleList = [tuple(map(str, i.split('$'))) for i in fileDrug]
drug = []
for entryDrugPrimaryID in drugTupleList:
	drug.append((entryDrugPrimaryID[0], entryDrugPrimaryID[5]))
fileDrug.close()

#Reading in the Reaction File into a List of Tuples, then Narrowing down to the Columns Required in a Tuple

with open('REAC20Q1.txt') as fileReaction:
	reactionTupleList = [tuple(map(str, i.split('$'))) for i in fileReaction]
reaction = []
for entryReacPrimaryID in reactionTupleList:
	reaction.append((entryReacPrimaryID[0], entryReacPrimaryID[2]))
fileReaction.close()

#Reading in the Outcomes File into a List of Tuples, then Narrowing down to the Columns Required in a Tuple

with open('OUTC20Q1.txt') as fileOutcomes:
	outcomesTupleList = [tuple(map(str, i.split('$'))) for i in fileOutcomes]
outcomes = []
for entryOutcomesPrimaryID in outcomesTupleList:
	outcomes.append((entryOutcomesPrimaryID[0], entryOutcomesPrimaryID[2]))
fileOutcomes.close()

#Starting to Use DataFrames and Pandas
#Converting above Tuples into DataFrames

##To Select Only the SaRS-CoV-2:
indicationDataFrame = pd.DataFrame(indication, columns = ['PrimaryID', 'Indication'])

interestindicationDataFrame = pd.DataFrame(indicationDataFrame.loc[indicationDataFrame['Indication'] == 'Corona virus infection\n'])

##For Drug, Reaction and Outcome Respectively:
drugNameDataFrame = pd.DataFrame(drug, columns = ['PrimaryID','Drug Name'])
reactionDataFrame = pd.DataFrame(reaction, columns = ['PrimaryID','Reaction'])
outcomesDataFrame = pd.DataFrame(outcomes, columns = ['PrimaryID','Outcomes'])

##Merging the Two DataFrames:
mergedDataFrame = interestindicationDataFrame.merge(drugNameDataFrame,on='PrimaryID').merge(reactionDataFrame,on='PrimaryID').merge(outcomesDataFrame,on='PrimaryID')
mergedDataFrame.to_csv('covid19.csv')
print('DoNe')
