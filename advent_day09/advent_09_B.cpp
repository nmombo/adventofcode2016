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

int findDecompLen(int numChars, int numTimes, string rest)
{
	int curLen = 0;
	for(int i = 0; i < numChars.length(); i++)
	{
		if(rest[i] == "(")
		{
			// Find the important indices for the compression marker
			int i_n1_start = chr+1;
			int i_x = input.find(chr, "x");
			int i_n2_start = i_x + 1;
			int i_cParen = input.find(chr, ")");
			// Find the key ints of the compression marker
			int nCharsToRpt = stoi(input.substr(i_n1_start, i_x - i_n1_start));
			int nTimesToRpt = stoi(input.substr(i_n2_start, i_cParen - i_n2_start));
			// Add the length of the decompressed data
			curLen += findDecompLen(nCharsToRpt, nTimesToRpt, input.substr(i_cParen+1)) * nTimesToRpt;
		}
		else
		{
			curLen++;
		}
	}
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
			// Add the length of the decompressed data
			chr_de += findDecompLen(nCharsToRpt, nTimesToRpt, input.substr(i_cParen+1)) * nTimesToRpt;
		}
		else
		{
			chr++;
			chr_de++;
		}
	}
}
