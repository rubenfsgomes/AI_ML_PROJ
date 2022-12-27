#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This struct represents a single stage in the rally, with its name and distance.
typedef struct {
  char* name;
  float distance;
} Stage;

// This struct represents a single competitor in the rally, with their number, name,
// car brand, and the times they recorded for each stage.
typedef struct {
  int number;
  char* name;
  char* car;
  int* times;
  int total_time;
  int num_valid_stages;
} Competitor;

// This struct represents the entire rally, with information about the number of
// competitors and stages, as well as an array of Stage structs and an array of
// Competitor structs.
typedef struct {
  int num_competitors;
  int num_stages;
  Stage* stages;
  Competitor* competitors;
} Rally;

// This function reads the stage data from the given file and returns an array of
// Stage structs with the information.
Stage* readStages(FILE* file, int num_stages) {
  Stage* stages = malloc(num_stages * sizeof(Stage));
  for (int i = 0; i < num_stages; i++) {
    stages[i].name = malloc(32 * sizeof(char)); // Allocate space for stage name.
    fscanf(file, "%s", stages[i].name); // Read stage name.
    fscanf(file, "%f", &stages[i].distance); // Read stage distance.
  }
  return stages;
}

// This function reads the competitor data from the given file and returns an array
// of Competitor structs with the information.
Competitor* readCompetitors(FILE* file, int num_competitors, int num_stages) {
  Competitor* competitors = malloc(num_competitors * sizeof(Competitor));
  for (int i = 0; i < num_competitors; i++) {
    competitors[i].times = malloc(num_stages * sizeof(int)); // Allocate space for stage times.
    competitors[i].name = malloc(32 * sizeof(char)); // Allocate space for competitor name.
    competitors[i].car = malloc(32 * sizeof(char)); // Allocate space for car brand.
    fscanf(file, "%d", &competitors[i].number); // Read competitor number.
    fscanf(file, "%s", competitors[i].name); // Read competitor name.
    fscanf(file, "%s", competitors[i].car); // Read car brand.
    competitors[i].total_time = 0; // Initialize total time to 0.
    competitors[i].num_valid_stages = 0; // Initialize number of valid stages to 0.
    for (int j = 0; j < num_stages; j++) {
      fscanf(file, "%d", &competitors[i].times[j]); // Read time for each stage.
      if (competitors[i].times[j] >= 0) { //
