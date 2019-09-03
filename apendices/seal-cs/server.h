#ifndef _SERVER_H_INCLUDED_
#define _SERVER_H_INCLUDED_

#include <iostream>
#include <fstream>      // std::ofstream

#include "seal/seal.h"
#include <vector>
#include <string>

#include "constants.h"
#include "common/sealfile.h"
#include "curva.h"

using namespace std;
using namespace seal;


class SServer {
  public:
    SServer();
    SServer(string config_mask);
    Ciphertext distance(Ciphertext x_encrypted, Ciphertext y_encrypted, RelinKeys relin_keys);
    void addCurva(Curva c);
    vector<string> getCurveNames();
  private:
    Evaluator* evaluator;
    CKKSEncoder* encoder;
    vector<Curva> curvas;
};

#endif
