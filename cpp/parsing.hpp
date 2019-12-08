// --------------------------------------------------------------------------
// Parsing: collection of string manipulation
// Author: Emmehandes
// License: MIT
// --------------------------------------------------------------------------
#ifndef PARSING_H
#define PARSING_H

#include <string>

#define WHITESPACE (" \t\n\r\f\v")

namespace parsing
{
  std::string& ltrim(std::string& s, const char* t = WHITESPACE);
  std::string& rtrim(std::string& s, const char* t= WHITESPACE);
  std::string& trim(std::string& s, const char* t = WHITESPACE);
  std::string& toLower(std::string& s);
  std::string& toUpper(std::string& s);
  std::string& findAndReplace(std::string& s,
                              std::string ToSearch,
                              std::string ReplaceStr);
  std::string& removeFromToken(std::string& str, std::string Token);
  uint32_t hexStrToUint(std::string& str);
}
#endif

