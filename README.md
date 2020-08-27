# Zip_and_Rename
 Programa que pode compactar/descompactar quaisquer arquivos com uma extensão especificada pelo usuário ou renomear tal extensão.
 Este script pode funcionar com qualquer tipo de arquivo. Contudo, ele foi criado especificamente para funcionar em conjunto com o programa [DManga](https://github.com/dkeas/DManga). Portanto, a disposição das pastas e subpastas devem obedecer um certo padrão.
 
 __Exemplo:__
 ```
└──...
    └─── Pasta central com todas as hqs/
         ├── Título hq1/
         │   ├── Capítulo1/
         │   │   ├── Página_1
         │   │   ├── Página_2
         │   │   └── ...
         │   └── Capítulo2/
         │       ├── Página_1
         │       ├── Página_2
         │       └── ...
         │   
         └── Título hq2/
             └── Capítulo1/
                 ├── Página_1
                 ├── Página_2
                 └── ...
                 
```
### Obs:
Se for digitado 'hq' quando o programa pergunta se o usuário quer compactar/descompactar arquivos, o programa iniciará com configurações predefinidas para histórias em quadrinhos, ou seja, compactará os arquivos de imagem por capítulos e os converterão em '.cbz'.

