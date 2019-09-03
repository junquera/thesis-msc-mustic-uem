#ifndef _CLIENT_H_INCLUDED_
#define _CLIENT_H_INCLUDED_

#include <iostream>
#include <fstream>      // std::ofstream


#include "seal/seal.h"
#include "constants.h"
#include "common/sealfile.h"

#include <vector>


#include "server.h"
#include "constants.h"

using namespace std;
using namespace seal;


class Distance {
  public:
    string name;
    double distance;

    Distance(string name, double distance) : name{name}, distance{distance} {
    }
};

class SClient {
  public:
    SClient();
    SClient(string config_mask);
    SClient(string config_mask, size_t poly_modulus_degree, vector<int> coeff_modulus);
    void genKeys();
    void setKeysFromFile(string keyFileName);
    Ciphertext encrypt(double a);
    Ciphertext encrypt(vector<double> a);
    vector<double> decrypt(Ciphertext a);
    void saveConfig();
    void saveConfig(string config_mask);
    PublicKey public_key;
    RelinKeys relin_keys;
    EncryptionParameters* parms;
  private:
    SecretKey secret_key;
    Encryptor* encryptor;
    Evaluator* evaluator;
    Decryptor* decryptor;
    CKKSEncoder* encoder;
    string config_mask;
};

#endif
