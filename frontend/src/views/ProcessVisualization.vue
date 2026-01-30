<template>
  <div class="process-visualization">
    <h1>流程可视化</h1>

    <!-- MetaMask连接状态 -->
    <div class="metamask-status">
      <button class="metamask-btn" @click="connectWallet" :disabled="isLoading">
        {{ walletConnected ? "已连接钱包" : "连接MetaMask" }}
      </button>
      <span v-if="walletConnected" class="wallet-address">{{
        walletAddress
      }}</span>
    </div>

    <!-- 时间线 -->
    <div class="timeline">
      <h3>发薪流程时间线</h3>
      <div class="timeline-container">
        <div
          v-for="(step, index) in processSteps"
          :key="index"
          class="timeline-item"
          :class="step.status"
        >
          <div class="timeline-marker">
            {{
              step.status === "completed"
                ? "✓"
                : step.status === "processing"
                  ? "⏳"
                  : "○"
            }}
          </div>
          <div class="timeline-content">
            <h4>{{ step.title }}</h4>
            <p class="timeline-description">{{ step.description }}</p>
            <p class="timeline-time">{{ step.time || "" }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 日志窗口 -->
    <div class="logs-window">
      <h3>流程日志</h3>
      <div class="logs-container">
        <div
          v-for="(log, index) in processLogs"
          :key="index"
          class="log-item"
          :class="log.level"
        >
          <span class="log-time">{{ log.time }}</span>
          <span class="log-level">{{ log.level.toUpperCase() }}</span>
          <span class="log-message">{{ log.message }}</span>
        </div>
        <div v-if="processLogs.length === 0" class="no-logs">暂无流程日志</div>
      </div>
    </div>

    <!-- 操作按钮 -->
    <div class="action-buttons">
      <button class="refresh-btn" @click="refreshProcess" :disabled="isLoading">
        {{ isLoading ? "刷新中..." : "刷新状态" }}
      </button>
      <button class="clear-btn" @click="clearLogs">清空日志</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import axios from "axios";

const isLoading = ref(false);
const walletConnected = ref(false);
const walletAddress = ref("");
const processSteps = ref([
  {
    title: "初始化流程",
    description: "系统准备发薪流程，验证参数",
    status: "pending",
    time: "",
  },
  {
    title: "HR创建工资单",
    description: "HR Agent 创建工资单并加密金额",
    status: "pending",
    time: "",
  },
  {
    title: "Payroll处理支付",
    description: "Payroll Agent 解密金额并执行支付",
    status: "pending",
    time: "",
  },
  {
    title: "Employee验证到账",
    description: "Employee Agent 验证支付到账情况",
    status: "pending",
    time: "",
  },
  {
    title: "生成最终报告",
    description: "系统生成发薪流程最终报告",
    status: "pending",
    time: "",
  },
]);

const processLogs = ref([]);

// MetaMask连接
const connectWallet = async () => {
  if (typeof window.ethereum === "undefined") {
    alert("请安装MetaMask钱包");
    return;
  }

  try {
    isLoading.value = true;
    // 请求连接钱包
    const accounts = await window.ethereum.request({
      method: "eth_requestAccounts",
    });

    walletAddress.value = accounts[0];
    walletConnected.value = true;

    // 检查网络
    await checkNetwork();

    processLogs.value.push({
      time: new Date().toLocaleString(),
      level: "success",
      message: `MetaMask钱包连接成功: ${walletAddress.value}`,
    });
  } catch (error) {
    console.error("连接钱包失败:", error);
    processLogs.value.push({
      time: new Date().toLocaleString(),
      level: "error",
      message: `连接钱包失败: ${error.message}`,
    });
  } finally {
    isLoading.value = false;
  }
};

// 检查网络
const checkNetwork = async () => {
  const chainId = await window.ethereum.request({ method: "eth_chainId" });
  const expectedChainId = "0x940"; // KiteAI Testnet (2368)

  if (chainId !== expectedChainId) {
    try {
      // 尝试切换网络
      await window.ethereum.request({
        method: "wallet_switchEthereumChain",
        params: [{ chainId: expectedChainId }],
      });
      processLogs.value.push({
        time: new Date().toLocaleString(),
        level: "success",
        message: "网络切换成功: KiteAI Testnet",
      });
    } catch (error) {
      console.error("网络切换失败:", error);
      processLogs.value.push({
        time: new Date().toLocaleString(),
        level: "error",
        message: `网络切换失败: ${error.message}`,
      });
    }
  } else {
    processLogs.value.push({
      time: new Date().toLocaleString(),
      level: "success",
      message: "当前网络正确: KiteAI Testnet",
    });
  }
};

// 获取流程状态
const getProcessStatus = async () => {
  isLoading.value = true;
  try {
    // 检查钱包连接状态
    if (!walletConnected.value) {
      await connectWallet();
    }

    // 这里可以从后端API获取流程状态
    // 暂时模拟流程执行
    simulateProcessExecution();
  } catch (error) {
    console.error("Failed to get process status:", error);
    processLogs.value.push({
      time: new Date().toLocaleString(),
      level: "error",
      message: "获取流程状态失败: " + error.message,
    });
  } finally {
    isLoading.value = false;
  }
};

// 模拟流程执行
const simulateProcessExecution = () => {
  let stepIndex = 0;

  const executeStep = () => {
    if (stepIndex < processSteps.value.length) {
      const step = processSteps.value[stepIndex];
      step.status = "processing";
      step.time = new Date().toLocaleString();

      processLogs.value.push({
        time: step.time,
        level: "info",
        message: `开始执行: ${step.title}`,
      });

      // 模拟步骤执行时间
      setTimeout(() => {
        step.status = "completed";
        processLogs.value.push({
          time: new Date().toLocaleString(),
          level: "success",
          message: `完成执行: ${step.title}`,
        });

        stepIndex++;
        executeStep();
      }, 1000);
    } else {
      // 流程完成
      processLogs.value.push({
        time: new Date().toLocaleString(),
        level: "success",
        message: "发薪流程完成，共成功发放 1 笔工资",
      });
    }
  };

  executeStep();
};

// 刷新流程状态
const refreshProcess = () => {
  getProcessStatus();
};

// 清空日志
const clearLogs = () => {
  processLogs.value = [];
};

// 监听URL参数，判断是否从发薪任务页跳转过来
const checkUrlParams = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const fromPayroll = urlParams.get("fromPayroll");
  if (fromPayroll === "true") {
    // 从发薪任务页跳转过来，自动开始流程
    getProcessStatus();
  }
};

onMounted(() => {
  checkUrlParams();
});
</script>

<style scoped>
.process-visualization {
  padding: 20px;
}

/* MetaMask连接状态 */
.metamask-status {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
  padding: 15px;
  background: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.metamask-btn {
  padding: 10px 20px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: #333;
  color: white;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
}

.metamask-btn:hover:not(:disabled) {
  background: #555;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.metamask-btn:disabled {
  background: #f5f5f5;
  color: #999;
  border: 1px solid #e0e0e0;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.wallet-address {
  font-family: "Courier New", monospace;
  font-size: 14px;
  color: #333;
  background: white;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  max-width: 300px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* 时间线样式 */
.timeline {
  margin-bottom: 30px;
}

.timeline h3 {
  margin-bottom: 20px;
  color: #333;
}

.timeline-container {
  position: relative;
  padding-left: 30px;
}

.timeline-container::before {
  content: "";
  position: absolute;
  left: 15px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #ddd;
}

.timeline-item {
  position: relative;
  margin-bottom: 30px;
  padding-left: 30px;
}

.timeline-marker {
  position: absolute;
  left: -30px;
  top: 0;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: bold;
  z-index: 1;
}

.timeline-item.completed .timeline-marker {
  background: #52c41a;
  color: white;
}

.timeline-item.processing .timeline-marker {
  background: #1890ff;
  color: white;
}

.timeline-item.pending .timeline-marker {
  background: #f0f0f0;
  color: #999;
}

.timeline-content {
  background: #f5f5f5;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.timeline-content h4 {
  margin-top: 0;
  margin-bottom: 5px;
  color: #333;
  font-size: 16px;
}

.timeline-description {
  margin: 5px 0;
  color: #666;
  font-size: 14px;
}

.timeline-time {
  margin: 5px 0 0 0;
  color: #999;
  font-size: 12px;
}

/* 日志窗口样式 */
.logs-window {
  margin-bottom: 30px;
}

.logs-window h3 {
  margin-bottom: 15px;
  color: #333;
}

.logs-container {
  background: #f5f5f5;
  border-radius: 8px;
  padding: 15px;
  max-height: 400px;
  overflow-y: auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.log-item {
  padding: 8px 0;
  border-bottom: 1px solid #eee;
  display: flex;
  font-family: "Courier New", monospace;
  font-size: 13px;
}

.log-item:last-child {
  border-bottom: none;
}

.log-time {
  color: #999;
  margin-right: 15px;
  min-width: 140px;
}

.log-level {
  margin-right: 15px;
  min-width: 70px;
  font-weight: bold;
}

.log-level.INFO {
  color: #1890ff;
}

.log-level.SUCCESS {
  color: #52c41a;
}

.log-level.ERROR {
  color: #ff4d4f;
}

.log-level.WARNING {
  color: #faad14;
}

.log-message {
  color: #333;
  flex: 1;
}

.no-logs {
  text-align: center;
  padding: 40px;
  color: #999;
}

/* 操作按钮 */
.action-buttons {
  display: flex;
  gap: 10px;
}

.refresh-btn,
.clear-btn {
  padding: 8px 16px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
  color: #333;
}

.refresh-btn:hover:not(:disabled),
.clear-btn:hover {
  background: #f5f5f5;
  border-color: #d0d0d0;
}

.refresh-btn:disabled {
  background: #f5f5f5;
  color: #999;
  cursor: not-allowed;
}
</style>
