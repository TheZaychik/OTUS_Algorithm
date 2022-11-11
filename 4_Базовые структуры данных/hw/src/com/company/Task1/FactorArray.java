package com.company.Task1;

public class FactorArray<T> implements IArray<T> {

    private Object[] array;
    private int factor;
    private int size;

    public FactorArray(int factor, int initLength) {
        this.factor = factor;
        array = new Object[initLength];
        size = 0;
    }

    public FactorArray() {
        this(50, 10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size() == array.length)
            resize();
        array[size] = item;
        size++;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T) array[index];
    }

    @Override
    public void add(T item, int index) {
        if (size() == array.length)
            resize();
        int j = 0;
        for (int i = size(); i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = item;
        size++;
    }

    @Override
    public T remove(int index) {
        Object[] newArray = new Object[size() - 1];
        var removed = (T) array[index];
        int j = 0;
        for (int i = 0; i < size(); i++) {
            if (i == index) {
                continue;
            }
            newArray[j] = array[i];
            j++;
        }
        array = newArray;
        return removed;
    }

    private void resize() {
        Object[] newArray = new Object[array.length + array.length * factor / 100];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }

//    public String toString() {
//        StringBuilder output = new StringBuilder();
//        output.append("[ ");
//        for (int i = 0; i < array.length; i++) {
//            output.append(array[i] == null ? "null " : array[i].toString() + " ");
//        }
//        output.append("]");
//        return output.toString();
//    }
}

