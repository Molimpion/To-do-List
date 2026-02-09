import { Header } from "./components/Header";
import './global.css';

export function App() {
  function addTask(taskTitle: string) {
    console.log("Nova tarefa digitada: ", taskTitle);
    alert(`Funcionou! Você tentou criar: ${taskTitle}`);
  }

  return (
    <>
      <Header onAddTask={addTask} />
      <div style={{ marginTop: '5rem', textAlign: 'center', color: 'white' }}>
         <p>A lista de tarefas vai aparecer aqui em breve.</p>
      </div>
    </>
  );
}