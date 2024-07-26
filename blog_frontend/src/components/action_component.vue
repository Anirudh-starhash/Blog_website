<template>
    <div class="abc">
        <main v-if="login_component" class="container">
            <form @submit.prevent="login">
              <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
          
              <div class="form-floating">
                <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="name">
                <label for="floatingInput">Name</label>
              </div>
              <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="email">
                <label for="floatingInput">Email address</label>
              </div>
              <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password" fdprocessedid="p1pgx" v-model="password">
                <label for="floatingPassword">Password</label>
              </div>
          
              <div class="form-check text-start my-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Remember me
                </label>
              </div>
              <button class="btn btn-primary w-100 py-2" type="submit" fdprocessedid="e845cp">Sign in</button>
    
            </form>
            <p>New Here? &nbsp; &nbsp; &nbsp; &nbsp; Sign Up </p>
        </main>
        <main v-if="register_component" class="container">
            <form @submit.prevent="register">
              <h1 class="h3 mb-3 fw-normal">Please sign up</h1>
          
              <div class="form-floating">
                <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="name">
                <label for="floatingInput">Name</label>
              </div>
              <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="email">
                <label for="floatingInput">Email Address</label>
              </div>
              <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password" fdprocessedid="p1pgx" v-model="password">
                <label for="floatingPassword">Password</label>
              </div>
              <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password" fdprocessedid="p1pgx" v-model="confirm_password">
                <label for="floatingPassword">Confirm-Password</label>
              </div>
          
              <div class="form-check text-start my-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                  Remember me
                </label>
              </div>
              <button class="btn btn-primary w-100 py-2" type="submit" fdprocessedid="e845cp">Sign up</button>
    
            </form>
            <p>Already a User? &nbsp; &nbsp; &nbsp; &nbsp;   Sign In</p>
           
        </main>
    </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
export default {
    name:'login_component',
    data(){
        return{
            email:"",
            password:"",
            name:"",
            confirm_password:""
        }
    },
    props:{
        login_component:{
            type:Boolean,
            default:false,
        },
        register_component:{
            type:Boolean,
            default:false,
        }
    },
    setup(){
        const router=useRouter();
        return {router};
    },
    methods:{
        async login(){
            try{
                const r=await axios.post("http://127.0.0.1:5000/api/user_login",
                    JSON.stringify({
                        'email':this.email,
                        'password':this.password
                    }),
                    {
                        headers:{
                            'Content-Type':'application/json'
                        }
                    }
                );

                if(r.status===200){
                    const access_token=r.data.access_token;
                    const info={
                        "email":r.data.info["email"],
                        "id":r.data.info["id"],
                        "role":r.data.info["role"],
                        "name":r.data.info["name"]
                    };
                    localStorage.setItem("access_token",access_token);
                    localStorage.setItem("info",JSON.stringify(info));
                    alert('Logged in Successfull!')
                    this.$router.push("/blogs")
                }
                else if(r.status===201){
                    alert('Not Registered Try Signup');
                }
                else{
                    alert('Password is wrong re-enter!')
                }
            }
            catch(error){
                alert(error);
            }
        },
        async register(){
          try{
            if(this.confirm_password!==this.password){
              alert('Password and Confirm Password didn\'t match')
              this.confirm_password="";
              this.$router.push("/register_page")
            }
            else{
            const response=await axios.post("http://127.0.0.1:5000/api/user_register",
              JSON.stringify({
                name:this.name,
                email:this.email,
                password:this.password,
                type:this.type,
                profile_pic:this.profile_pic
              }),{
                headers:{
                  'Content-Type':'application/json'
                }
              }
            );

            if(response.status===200){
              alert('Successfully logged in! Go to SignInto login')
            }
            else{
              alert('Already Registered! Try SignIn!')
            }}
          }
          catch(error){
            console.log(error);
          }
        },
    }
}
</script>

<style scoped>
  .abc{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items:center;
    background-color:#0f172a;
    width:50%;
    padding:1.5rem;
  }
  .container{
    display:flex;
    flex-direction: column;;
    gap:20px;
  }
  h1{
    color:#818cf8;
  }
  label{
    color:white;
  }
  .form-floating label{
    color:black;
    font-weight:bold;
  }
  form{
    display: flex;
    flex-direction: column;
    gap:20px;
  }
  p{
    color:white;
  }
</style>