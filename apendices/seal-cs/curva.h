#ifndef _CURVA_H_INCLUDED_
#define _CURVA_H_INCLUDED_

#include <string>
#include <vector>
#include <iostream>
#include <fstream>      // std::ofstream

using namespace std;

class Curva {
  public:
    double a, b, c;
    std::string name = "";
    Curva(double a, double b, double c) : a{a}, b{b}, c{c} {
    }

    Curva(std::string name, double a, double b, double c) 
	 : name{name}, a{a}, b{b}, c{c} {
    }
};


inline void saveCurveNames(vector<Curva> curvas, string filename){
  ofstream res;
  res.open(filename);

  for(Curva c: curvas)
    res << c.name << endl;

  res.close();
};


inline void saveCurveNames(vector<string> curvas, string filename){
  ofstream res;
  res.open(filename);

  for(string name: curvas)
    res << name << endl;

  res.close();
};


inline vector<string> loadCurveNames(string filename){
  vector<string> names;
  string line;
  ifstream res(filename);
  if (res.is_open()) {
    while ( getline (res, line) ) {
      names.push_back(line);
      cout << line << '\n';
    }
    res.close();
  }
  return names;
};



#endif
