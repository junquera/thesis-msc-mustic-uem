#ifndef _SERVER_H_INCLUDED_
#define _SERVER_H_INCLUDED_

#include "common/hefile.h"
#include "reg2.h"

class HServer {
  public:
    HServer(int _nb_bits, int _float_bits);
    // TODO cloud_key_path > bk
    void regresionCuadratica(LweSample* a, LweSample* b, LweSample* c, const vector<LweSample*> xs, const vector<LweSample*> ys, string cloud_key_path, string results_path);
  private:
    int nb_bits;
    int float_bits;
};

#endif
