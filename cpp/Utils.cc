// --------------------------------------------------------------------------
// Utils: collection of string manipulation
// Author: Maeltrine
// License: MIT
// --------------------------------------------------------------------------
#include <iomanip>
#include <algorithm>
#include "Utils.hpp"

namespace utils
{

/* @Trim from left side
----------------------------------------------------------------------------- */
std::string& ltrim(std::string& s, const char* t)
{
    s.erase(0, s.find_first_not_of(t));
    return s;
}

/* @Trim from right side
----------------------------------------------------------------------------- */
std::string& rtrim(std::string& s, const char* t)
{
    s.erase(s.find_last_not_of(t) + 1);
    return s;
}

/* @Trim from right and left sides
----------------------------------------------------------------------------- */
std::string& trim(std::string& s, const char* t)
{
    return ltrim(rtrim(s, t), t);
}

/* @Convert string to lower case
----------------------------------------------------------------------------- */
std::string& toLower(std::string& s)
{
	std::transform(s.begin(),s.end(), s.begin(), ::tolower);
	return s;
}

/* @Convert string to upper case
----------------------------------------------------------------------------- */
std::string& toUpper(std::string& s)
{
	std::transform(s.begin(),s.end(), s.begin(), ::toupper);
	return s;
}

/* @Find a string and replace it with another one
----------------------------------------------------------------------------- */
std::string& findAndReplace(std::string& s,
										 std::string ToSearch,
										 std::string ReplaceStr)
{
	size_t pos = s.find(ToSearch);
	s.replace(pos,ToSearch.size(), ReplaceStr);
	return s;
}
/* @Delete everything in a string starting from a token
***************************************************************************** */
std::string& removeFromToken(std::string& str, std::string Token)
{
	size_t cmt_start = str.find(Token);
	str = str.substr(0,cmt_start);
	return str;
}

/* @Convert hexadecimal string to UINT number
***************************************************************************** */
uint32_t hexToUint(std::string& str)
{
	uint32_t val=0xFFFFFFFF;

	trim(str);
	if("NAN" != str)
	{
		val = std::stoi(str,nullptr,0);
	}
	return val;
}

}
