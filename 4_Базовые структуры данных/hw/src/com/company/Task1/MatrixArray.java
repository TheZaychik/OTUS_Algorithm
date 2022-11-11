package com.company.Task1;

public class MatrixArray<T> implements IArray<T> {

    private int size;
    private int vector;
    private IArray<IArray<T>> array;

    public MatrixArray(int vector) {
        this.vector = vector;
        array = new SingleArray<>();
        size = 0;
    }

    public MatrixArray() {
        this(10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size == array.size() * vector)
            array.add(new VectorArray<T>(vector));
        array.get(size / vector).add(item);
        size++;
    }

    @Override
    public T get(int index) {
        return array.get(index / vector).get(index % vector);
    }

    @Override
    public void add(T item, int index) {
        if (size == array.size() * vector)
            array.add(new VectorArray<T>(vector));
        array.get(size / vector).add(item, index);
        size++;
    }

    @Override
    public T remove(int index) {
        size--;
        return array.get(size / vector).remove(index);
    }

//    public String toString() {
//        StringBuilder output = new StringBuilder();
//        for (int i = 0; i < array.size(); i++) {
//            output.append("[ ");
//            for (int j = 0; j < array.get(size / vector).size(); j++) {
//                output.append(array.get(size / vector).get(i) == null ? "null " : array.get(size / vector).get(i).toString() + " ");
//            }
//            output.append("]\n");
//        }
//        return output.toString();
//    }
}