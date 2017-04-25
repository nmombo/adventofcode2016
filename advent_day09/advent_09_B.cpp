#include <iostream>
#include <fstream>
using namespace std;

// Writes the input string to parameter
void readFile(string& in)
{
	ifstream inFile;
	inFile.open("advent_09.txt");
	inFile >> in;
	inFile.close();
}

int main()
{
	// READ INPUT FROM FILE
	string input;
	readFile(input);

	// LOOP THROUGH INPUT TO SUM DECOMPRESSED LENGTH
	int chr = 0;
	int chr_de = 0;
	while(chr < input.length())
	{
		if (input[chr] == "(")
		{
			// Find the important indices for the compression marker
			int i_n1_start = chr + 1;
			int i_x = input.find(chr, "x");
			int i_n2_start = i_x + 1;
			int i_cParen = input.find(chr, ")");
			// Find the key ints of the compression marker
			int nCharsToRpt = stoi(input.substr(i_n1_start, i_x - i_n1_start));
			int nTimesToRpt = stoi(input.substr(i_n2_start, i_cParen - i_n2_start));
			// Find the characters that need to be repeated
			string charsToRepeat = input.substr(i_cParen+1, nCharsToRpt);
			// Repeat the characters
			string stringToInsert = charsToRepeat;
			for (int i = 0; i < nCharsToRpt-1; i++)
			{
				stringToInsert += charsToRepeat;
			}
			// Insert the repeated characters into the string and remove the compression marker
			input = input.substr(0, chr) + stringToInsert + input.substr(i_cParen+charsToRepeat.length()+1);
			// Iterate by skipping to the end of the inserted string
			chr += nCharsToRpt * nTimesToRpt;
		}
		else
		{
			chr++;
		}
	}
}
