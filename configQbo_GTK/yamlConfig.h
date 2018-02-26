#ifndef YAML_CONFIG_H
#define YAML_CONFIG_H

typedef struct YAMLconfig {
  int age;
  char language[80];
  char startWith[80];
  char tokenAPIai[256];
}YAMLconfig;

int readConfig(YAMLconfig* conf);
int writeConfig(YAMLconfig* conf);


#endif
