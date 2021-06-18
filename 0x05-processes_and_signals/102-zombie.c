#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - sudo me 5 zombies
 *
 * Return: 0, per usual
 */
int main(void)
{
  pid_t pid;
  unsigned int x;

  for (x = 0; x < 5; x++)
    {
      pid = fork();
      if (pid == 0)
	exit(0);
      printf("Zombie process created, PID: %d\n", pid);
    }
  infinite_while();
  return (0);
}

/**
 * infinite_while - Kills zombies
 *
 * Return: 0
 */
int infinite_while(void)
{
  while (1)
    {
      sleep(1);
    }
  return (0);
}
