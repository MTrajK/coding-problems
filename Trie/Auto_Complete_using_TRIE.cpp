// C++ program to demonstrate auto-complete feature 
// using Trie data structure. 
#include<bits/stdc++.h> 
using namespace std; 

// Alphabet size (# of symbols) 
#define ALPHABET_SIZE (26) 

// Converts key current character into index 
// use only 'a' through 'z' and lower case 
#define CHAR_TO_INDEX(c) ((int)c - (int)'a') 

// trie node 
struct TrieNode 
{ 
	struct TrieNode *children[ALPHABET_SIZE]; 

	// isWordEnd is true if the node represents 
	// end of a word 
	bool isWordEnd; 
}; 

// Returns new trie node (initialized to NULLs) 
struct TrieNode *getNode(void) 
{ 
	struct TrieNode *pNode = new TrieNode; 
	pNode->isWordEnd = false; 

	for (int i = 0; i < ALPHABET_SIZE; i++) 
		pNode->children[i] = NULL; 

	return pNode; 
} 

// If not present, inserts key into trie. If the 
// key is prefix of trie node, just marks leaf node 
void insert(struct TrieNode *root, const string key) 
{ 
	struct TrieNode *pCrawl = root; 

	for (int level = 0; level < key.length(); level++) 
	{ 
		int index = CHAR_TO_INDEX(key[level]); 
		if (!pCrawl->children[index]) 
			pCrawl->children[index] = getNode(); 

		pCrawl = pCrawl->children[index]; 
	} 

	// mark last node as leaf 
	pCrawl->isWordEnd = true; 
} 

// Returns true if key presents in trie, else false 
bool search(struct TrieNode *root, const string key) 
{ 
	int length = key.length(); 
	struct TrieNode *pCrawl = root; 
	for (int level = 0; level < length; level++) 
	{ 
		int index = CHAR_TO_INDEX(key[level]); 

		if (!pCrawl->children[index]) 
			return false; 

		pCrawl = pCrawl->children[index]; 
	} 

	return (pCrawl != NULL && pCrawl->isWordEnd); 
} 

// Returns 0 if current node has a child 
// If all children are NULL, return 1. 
bool isLastNode(struct TrieNode* root) 
{ 
	for (int i = 0; i < ALPHABET_SIZE; i++) 
		if (root->children[i]) 
			return 0; 
	return 1; 
} 

// Recursive function to print auto-suggestions for given 
// node. 
void suggestionsRec(struct TrieNode* root, string currPrefix) 
{ 
	// found a string in Trie with the given prefix 
	if (root->isWordEnd) 
	{ 
		cout << currPrefix; 
		cout << endl; 
	} 

	// All children struct node pointers are NULL 
	if (isLastNode(root)) 
		return; 

	for (int i = 0; i < ALPHABET_SIZE; i++) 
	{ 
		if (root->children[i]) 
		{ 
			// append current character to currPrefix string 
			currPrefix.push_back(97 + i); 

			// recur over the rest 
			suggestionsRec(root->children[i], currPrefix); 
		} 
	} 
} 

// print suggestions for given query prefix. 
int printAutoSuggestions(TrieNode* root, const string query) 
{ 
	struct TrieNode* pCrawl = root; 

	// Check if prefix is present and find the 
	// the node (of last level) with last character 
	// of given string. 
	int level; 
	int n = query.length(); 
	for (level = 0; level < n; level++) 
	{ 
		int index = CHAR_TO_INDEX(query[level]); 

		// no string in the Trie has this prefix 
		if (!pCrawl->children[index]) 
			return 0; 

		pCrawl = pCrawl->children[index]; 
	} 

	// If prefix is present as a word. 
	bool isWord = (pCrawl->isWordEnd == true); 

	// If prefix is last node of tree (has no 
	// children) 
	bool isLast = isLastNode(pCrawl); 

	// If prefix is present as a word, but 
	// there is no subtree below the last 
	// matching node. 
	if (isWord && isLast) 
	{ 
		cout << query << endl; 
		return -1; 
	} 

	// If there are are nodes below last 
	// matching character. 
	if (!isLast) 
	{ 
		string prefix = query; 
		suggestionsRec(pCrawl, prefix); 
		return 1; 
	} 
} 

// Driver Code 
int main() 
{ 
	struct TrieNode* root = getNode(); 
	insert(root, "hello"); 
	insert(root, "dog"); 
	insert(root, "hell"); 
	insert(root, "cat"); 
	insert(root, "a"); 
	insert(root, "hel"); 
	insert(root, "help"); 
	insert(root, "helps"); 
	insert(root, "helping"); 
	int comp = printAutoSuggestions(root, "hel"); 

	if (comp == -1) 
		cout << "No other strings found with this prefix\n"; 

	else if (comp == 0) 
		cout << "No string found with this prefix\n"; 

	return 0; 
} 
