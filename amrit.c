#include<stdio.h>
#include<stdlib.h>

struct Node{
  int data;
  struct Node*next;
};

struct Node*createNode(int value){
  struct Node*new_node = malloc(sizeof(struct Node));
  if(!new_node){
    printf("Memory allocaiton is failed!!");
    exit(1);
  };

  new_node->data = value;
  new_node->next = NULL;
  return new_node;
};


void insertBeg(struct Node**head, int value){
  struct Node*new_node = createNode(value);
  new_node->next = *head;
  *head = new_node;

}


void insertEnd(struct Node**head, int value){
  struct Node*new_node = createNode(value);
  if (*head == NULL){
    *head = new_node;
    return;
  }

  struct Node*temp = *head;
  while (temp->next != NULL)
  {
    temp = temp->next;
  };
  temp->next = new_node;
  
}

void traversse(struct Node*head){
  struct Node*temp = head;
  while ( temp)
  {
    printf("%d-->",temp->data);
    temp = temp->next;
  };

  printf("Node");
  
}


int main(){

  struct Node*head = NULL;
  insertBeg(&head,1);
  traversse(head);
  return 0;
}