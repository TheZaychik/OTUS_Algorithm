package com.company;

import com.company.Task1.FactorArray;
import com.company.Task1.IArray;
import com.company.Task1.SingleArray;
import com.company.Task1.VectorArray;
import com.company.Task1.MatrixArray;
import com.company.Task2.ArrayListWrapper;
import com.company.Task3.PriorityQueue;

import java.util.Date;

public class Main {

    @SuppressWarnings("unchecked")
    private static void Task1() {
        System.out.println("SingleArray");
        IArray SingleArray = new SingleArray();
        SingleArray.add("a");
        SingleArray.add("b");
        SingleArray.add("c", 0);
        System.out.println(SingleArray);
        System.out.println(SingleArray.remove(1));
        System.out.println(SingleArray);
        System.out.println("VectorArray");
        IArray VectorArray = new VectorArray();
        VectorArray.add("a");
        VectorArray.add("b");
        System.out.println(VectorArray);
        VectorArray.add("c", 0);
        System.out.println(VectorArray);
        System.out.println(VectorArray.remove(1));
        System.out.println(VectorArray);
        System.out.println("FactorArray");
        IArray FactorArray = new FactorArray();
        FactorArray.add("a");
        FactorArray.add("b");
        System.out.println(FactorArray);
        FactorArray.add("c", 0);
        System.out.println(FactorArray);
        System.out.println(FactorArray.remove(1));
        System.out.println(FactorArray);
        System.out.println("MatrixArray");
        IArray MatrixArray = new MatrixArray();
        MatrixArray.add("a");
        MatrixArray.add("b");
        System.out.println(MatrixArray);
        MatrixArray.add("c", 0);
        System.out.println(MatrixArray);
        System.out.println(MatrixArray.remove(1));
        System.out.println(MatrixArray);


    }

    private static void testArray(ArrayListWrapper data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j++)
            data.add(new Date());

        System.out.println(data + " testArray: " +
                (System.currentTimeMillis() - start));
    }

    private static void testArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j++)
            data.add(new Date());

        System.out.println(data + " testArray: " +
                (System.currentTimeMillis() - start));
    }


    private static void Task2() {
        for (int total = 1_000; total <= 100_000; total *= 10) {
            System.out.println("Таблица сравнения производительности");
            System.out.println("Кол-во элементов - " + total);
            IArray singleArray = new SingleArray();
            IArray vectorArray = new FactorArray();
            IArray factorArray = new FactorArray();
            IArray matrixArray = new MatrixArray();
            ArrayListWrapper<Date> ArrayListWrapper = new ArrayListWrapper<>();
            testArray(singleArray, total);
            testArray(vectorArray, total);
            testArray(factorArray, total);
            testArray(matrixArray, total);
            testArray(ArrayListWrapper, total);
        }
    }

    private static void Task3() {
        PriorityQueue<String> pq = new PriorityQueue<>();
        pq.enqueue(0, "Первый в очереди с приоритеом 0");
        pq.enqueue(0, "Второй в очереди с приоритеом 0");
        pq.enqueue(1, "Первый в очереди с приоритеом 1");
        pq.enqueue(1, "Второй в очереди с приоритеом 1");
        System.out.println(pq.dequeue());
        System.out.println(pq.dequeue());
        System.out.println(pq.dequeue());
        System.out.println(pq.dequeue());
    }

    public static void main(String[] args) {
//        Task1();
//        Task2();
        Task3();

    }

}
