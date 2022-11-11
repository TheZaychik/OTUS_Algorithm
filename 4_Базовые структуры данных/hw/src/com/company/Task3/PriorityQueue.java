package com.company.Task3;


import com.company.Task1.SingleArray;

public class PriorityQueue<T> {
    private SingleArray<Queue<T>> array;

    public PriorityQueue(int priorityCount) {
        array = new SingleArray<>();
        for (int i = 0; i < priorityCount; i++) {
            array.add(new Queue<>());
        }
    }

    public PriorityQueue() {
        this(3);
    }

    public void enqueue(int priority, T item) {
        array.get(priority).enqueue(item);
    }

    public T dequeue() {
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i).size() > 0) {
                return array.get(i).dequeue();
            }
        }
        return null;
    }
}
