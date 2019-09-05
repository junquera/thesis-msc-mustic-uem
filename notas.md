# Librerías

Centrarse en (decidir por qué):

## Partially...

- BGV: HELib
- BFV: SEAL
- BGV y BFV: PALISADE

Usaremos SEAL como "representante" de las segunda generación. 

- PALISADE (son las cubiertas en http://homomorphicencryption.org/wp-content/uploads/2018/10/CCS-HE-Tutorial-Slides.pdf)

## Fully...

- GSW: FHEW / TFHE 

Mejor TFHE(-Chimera) (cubre dos modelos)

# Análisis

## SEAL

Recommendation: Learn BFV scheme first; CKKS after that
> https://arxiv.org/pdf/1906.07127.pdf

## PALISADE

https://medium.com/privacy-preserving-natural-language-processing/homomorphic-encryption-for-beginners-a-practical-guide-part-1-b8f26d03a98a

## TFHE

Tutorial: https://tfhe.github.io/tfhe/coding.html

# Notas

## Modelado de datos (https://medium.com/privacy-preserving-natural-language-processing/homomorphic-encryption-for-beginners-a-practical-guide-part-1-b8f26d03a98a)

- BGV y BFV computations can only be performed on integers

- CKKS: Computations can be performed on complex numbers

## Multi party diffie hellman

https://www.di.ens.fr/david.pointcheval/Documents/Papers/2002_sac.pdf

## cuFHE

Es como TFHE pero con wrapper en python: 

https://github.com/vernamlab/cuFHE
