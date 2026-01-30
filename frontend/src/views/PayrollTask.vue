<template>
  <div class="payroll-task">
    <h1>发薪流程</h1>

    <div class="payroll-options">
      <h3>核心支付流程</h3>
      <p>HR Agent → Payroll Agent → Employee Agent</p>
      <button
        class="submit-btn"
        @click="startPayrollProcess"
        :disabled="isSubmitting"
      >
        {{ isSubmitting ? "处理中..." : "启动发薪流程" }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const isSubmitting = ref(false);

// 启动发薪流程
const startPayrollProcess = async () => {
  isSubmitting.value = true;
  try {
    // 简化版本：使用固定的员工数据
    const employees = [
      {
        id: "emp001",
        name: "Employee",
        address: "0x1122334455667788990011223344556677889900",
        amount: "10000",
      },
    ];

    const response = await axios.post("http://localhost:3000/api/runPayroll", {
      employees: employees,
    });

    console.log("Payroll process started:", response.data);
    // 跳转到流程可视化页面，添加参数标识来自发薪任务页
    window.location.href = "/process?fromPayroll=true";
  } catch (error) {
    console.error("Failed to start payroll process:", error);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.payroll-task {
  padding: 20px;
  text-align: center;
}

.payroll-task h1 {
  margin-bottom: 30px;
  color: #333;
}

.payroll-options {
  max-width: 600px;
  margin: 0 auto;
  background: #f5f5f5;
  border-radius: 8px;
  padding: 40px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.payroll-options h3 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #333;
  font-size: 18px;
}

.payroll-options p {
  margin-bottom: 30px;
  color: #666;
  font-size: 16px;
}

.submit-btn {
  background: #333;
  color: #fff;
  border: none;
  border-radius: 12px;
  padding: 15px 30px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.submit-btn:hover:not(:disabled) {
  background: #555;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.submit-btn:disabled {
  background: #f5f5f5;
  color: #999;
  border: 1px solid #e0e0e0;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}
</style>
